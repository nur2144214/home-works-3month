from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import cancel, size_keyboard

class store(StatesGroup):
    product_name = State()
    size = State()
    price = State()
    category = State()
    product_photo = State()

async def start_fsm(message: types.Message):
    await message.answer("введите название товара:", reply_markup=cancel)
    await store.product_name.set()

async def load_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text
    await store.next()
    await message.answer("введите/выберите размер товара:", reply_markup=size_keyboard())
async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await store.next()
    await message.answer("введите цену товара:", reply_markup=cancel)

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await store.next()
    await message.answer("введите категорию товара:", reply_markup=cancel)

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await store.next()
    await message.answer("отправьте фото товара", reply_markup=cancel)

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data['photo'], caption=f"имя товара - {data['product_name']}\n"
                         f"размер товра - {data['size']}\n"
                         f"цена товара - {data['price']}\n"
                                                            f"категория товара - {data['category']}")
    await state.finish()

async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('отменено')

def reg_handler_fsm_registration(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(start_fsm, commands=['registration'])
    dp.register_message_handler(load_product_name, state=store.product_name)
    dp.register_message_handler(load_size, state=store.size)
    dp.register_message_handler(load_price, state=store.price)
    dp.register_message_handler(load_category, state=store.category)
    dp.register_message_handler(load_photo,state=store.product_photo, content_types=["photo"])