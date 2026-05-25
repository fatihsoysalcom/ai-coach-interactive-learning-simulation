import time

def ai_coach_response(user_input: str, conversation_history: list) -> str:
    """
    Simulates an AI coach's response based on user input and conversation history.
    In a real GenaAIGemmaCoach application, this function would integrate with
    a large language model (like Google's Gemma) to generate dynamic,
    context-aware, and personalized responses.
    """
    user_input_lower = user_input.lower()
    
    # Simple state management for a basic learning path
    # The last item in history might contain the current topic or context.
    current_context = conversation_history[-1] if conversation_history else {}
    current_topic = current_context.get("topic")
    
    if not conversation_history:
        # Initial greeting
        return "Merhaba! Ben GenaAIGemmaCoach. Bugün hangi konuda öğrenmek istersin? Örneğin, 'Yapay Zeka nedir?' diye sorabilirsin."

    # --- Simulate AI Coach Logic (where a real LLM would be integrated) ---
    # This section uses simple keyword matching and state to mimic an AI coach.
    # A real LLM like Gemma would understand nuances, generate creative responses,
    # and maintain a much richer context.

    if "yapay zeka" in user_input_lower or "ai" in user_input_lower or "artificial intelligence" in user_input_lower:
        if current_topic != "yapay_zeka_intro":
            conversation_history.append({"topic": "yapay_zeka_intro"})
            return ("Yapay zeka (YZ), makinelerin insan zekasını taklit etmesini sağlayan bir teknoloji alanıdır. "
                    "Öğrenme, problem çözme, algılama ve dil anlama gibi yetenekleri içerir. "
                    "Sence yapay zeka günlük hayatımızda nerelerde kullanılıyor?")
        elif "kullanım" in user_input_lower or "nerede" in user_input_lower or "örnek" in user_input_lower:
            if current_topic != "yapay_zeka_usage":
                conversation_history.append({"topic": "yapay_zeka_usage"})
                return ("Çok doğru! Akıllı telefonlar, öneri sistemleri, otonom araçlar, sağlık teşhisleri... "
                        "Peki, yapay zekanın temel bileşenlerinden bazılarını biliyor musun? "
                        "Örneğin, 'makine öğrenmesi' veya 'derin öğrenme' gibi.")
            else:
                return "Evet, bu alanlar yapay zekanın günlük hayattaki önemli kullanım alanlarıdır. Başka bir örnek düşünebiliyor musun?"
        elif "makine öğrenmesi" in user_input_lower or "derin öğrenme" in user_input_lower or "bileşen" in user_input_lower:
            if current_topic != "yapay_zeka_components":
                conversation_history.append({"topic": "yapay_zeka_components"})
                return ("Makine öğrenmesi (ML), yapay zekanın bir alt kümesidir ve makinelerin açıkça programlanmadan verilerden öğrenmesini sağlar. "
                        "Derin öğrenme ise ML'nin bir alt kümesi olup, yapay sinir ağları kullanarak daha karmaşık desenleri öğrenir. "
                        "Bu konularda daha fazla bilgi almak ister misin?")
            else:
                return "Makine öğrenmesi ve derin öğrenme, yapay zekanın temel taşlarıdır. Başka bir bileşen hakkında konuşmak ister misin?"
        else:
            return "Yapay zeka hakkında daha spesifik ne öğrenmek istersin? Örneğin, 'YZ'nin faydaları nelerdir?' diye sorabilirsin."

    elif "teşekkür" in user_input_lower or "sağ ol" in user_input_lower:
        return "Rica ederim! Başka bir konuda yardıma ihtiyacın olursa buradayım."
    
    elif "çıkış" in user_input_lower or "bitir" in user_input_lower:
        return "Görüşmek üzere! Öğrenme yolculuğunda başarılar dilerim."

    # Default response if no specific keywords are matched
    return ("Anladım. Başka bir konuda mı konuşmak istersin, yoksa mevcut konuya devam mı edelim? "
            "Ne hakkında daha fazla bilgi almak istediğini açıkça belirtir misin?")

def main():
    print("GenaAIGemmaCoach'a hoş geldin! (Çıkmak için 'çıkış' yazın)")
    print("-" * 50)

    conversation_history = []
    
    # Initial coach message
    coach_message = ai_coach_response("", conversation_history)
    print(f"Coach: {coach_message}")

    while True:
        user_input = input("Sen: ")
        if user_input.lower() in ["çıkış", "exit", "bitir", "quit"]:
            print("Coach: Görüşmek üzere! Öğrenme yolculuğunda başarılar dilerim.")
            break
        
        # Simulate thinking time for a more natural interaction
        time.sleep(1) 
        
        coach_message = ai_coach_response(user_input, conversation_history)
        print(f"Coach: {coach_message}")

if __name__ == "__main__":
    main()
