from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def video_intro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Сообщение 1
    await update.message.reply_text(
        "🎬 *Стань Ближе*: яркие эмоции, теплое общение и музыка, объединяющая сердца!\n\n"
        "Мечтаете о крепкой связи со своим ребёнком, а он сидит в гаджетах?\n"
        "Хотите создать нечто особенное, что останется с вами на всю жизнь?\n\n"
        "Представьте: вы и ваш ребёнок в профессиональной студии, записываете песню, "
        "а потом снимаете клип! Это не просто развлечение, а настоящий совместный опыт.",
        parse_mode="Markdown"
    )

    # Сообщение 2 — видео
    with open("intro.mp4", "rb") as video:
        await update.message.reply_video(
            video=video,
            caption="⬆️ Это краткое видео о проекте *«Стань Ближе»*",
            parse_mode="Markdown"
        )

    # Сообщение 3 — для кого проект
    await update.message.reply_text(
        "*Проект «Стань Ближе» идеально подойдёт для:*\n"
        "• 👨‍👩‍👧 Родителей и детей-подростков — создайте уникальный семейный шедевр\n"
        "• 💑 Пар — запишите песню, отражающую вашу любовь и историю\n"
        "• 👥 Коллективов — сделайте корпоративное поздравление с душой и креативом",
        parse_mode="Markdown"
    )

    # Сообщение 4 — преимущества
    await update.message.reply_text(
        "*Наши преимущества:*\n"
        "• ❤️ Незабываемые тёплые эмоции: душевная атмосфера и вдохновение\n"
        "• 🎧 Лучшее оборудование: профессиональный звук\n"
        "• 🎉 Удобное время: сделайте выходной незабываемым\n"
        "• 🎬 Клип на память: всё в профессиональном формате",
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token("ТВОЙ_ТОКЕН").build()
app.add_handler(CommandHandler("video", video_intro))
app.run_polling()
