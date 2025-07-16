from aiogram import Router, F
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, CallbackQuery

donate_router = Router()

@donate_router.callback_query(F.data == "subscribe_99")
async def subscribe_callback(callback: CallbackQuery):
    prices = [LabeledPrice(label="Подписка", amount=99)]
    await callback.message.answer_invoice(
        title="Подписка на уведомления",
        description="Подписка действует 30 дней и стоит 99 звёзд",
        provider_token="",
        currency="XTR",
        prices=prices,
        payload="subscribe_99"
    )
    await callback.answer()

@donate_router.pre_checkout_query()
async def pre_checkout(pre_checkout_q: PreCheckoutQuery):
    await pre_checkout_q.answer(ok=True)

@donate_router.message(F.successful_payment)
async def on_success(message: Message):
    t_id = message.successful_payment.telegram_payment_charge_id
    await message.answer(
        "📬 <b>Подписка на уведомления о новых подарках</b>\n"
        "Подписка действует 30 дней и стоит 99 звёзд\n"
        f"<i>Транзакция:</i> <code>{t_id}</code>"
    )
