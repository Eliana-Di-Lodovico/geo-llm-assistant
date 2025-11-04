"""
Simple example demonstrating the GeoResearch Assistant.
Run this script to see the assistant in action without Jupyter.
"""
from geo_assistant import GeoAssistant
from data import get_dataset, get_dataset_info


def main():
    """Main function to demonstrate the GeoResearch Assistant."""
    print("=" * 60)
    print("GeoResearch Assistant Demo")
    print("=" * 60)
    
    # Show dataset info
    dataset_info = get_dataset_info()
    print(f"\n📚 Dataset: {dataset_info['num_documents']} documents")
    print(f"📋 Topics: {', '.join(dataset_info['topics'][:3])}...")
    
    # Initialize assistant
    print("\n🤖 Initializing GeoResearch Assistant...")
    assistant = GeoAssistant()
    
    # Load knowledge base
    documents = get_dataset()
    assistant.load_knowledge_base(documents)
    
    kb_info = assistant.get_knowledge_base_info()
    print(f"✅ Knowledge base ready: {kb_info['num_documents']} documents")
    
    # Example questions
    questions = [
        "What is the highest mountain in the world?",
        "Which is the largest ocean on Earth?",
        "How much have global temperatures increased?",
        "What is special about the Amazon rainforest?",
    ]
    
    print("\n" + "=" * 60)
    print("Asking Questions")
    print("=" * 60)
    
    for i, question in enumerate(questions, 1):
        print(f"\n❓ Question {i}: {question}")
        result = assistant.ask(question, top_k=2)
        print(f"💡 Answer: {result['answer']}")
    
    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)
    print("\nFor more interactive examples, check out demo.ipynb")


if __name__ == "__main__":
    main()
