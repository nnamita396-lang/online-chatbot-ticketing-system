def get_bot_response(message):
    text = message.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! I am the Ticket Support Bot. How can I help you?"

    if "book" in text or "ticket" in text:
        return "You can create a ticket from the 'Create Ticket' page. Please provide your contact details and issue."

    if "status" in text:
        return "You can check your ticket status from the 'View Tickets' page in this student project."

    if "payment" in text or "pay" in text:
        return "For payment-related problems, select 'Payment' as the category while creating a ticket."

    if "login" in text or "password" in text:
        return "For login or password problems, create a ticket under the 'Account' category."

    if "refund" in text:
        return "For refund-related queries, create a ticket and explain your issue clearly."

    if "contact" in text or "support" in text:
        return "Please create a support ticket. Our support team can check the issue and update its status."

    if "thank" in text:
        return "You're welcome! Have a nice day."

    return "Sorry, I did not understand that. You can ask about tickets, payment, login, refund, or support."
