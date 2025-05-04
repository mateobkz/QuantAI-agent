import os
import matplotlib.pyplot as plt


def plot_predictions(real, predicted, model_name='Model'):
    """
    Affiche un graphe des vraies valeurs vs. les prédictions.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(real, label='Real', color='blue', marker='o')
    plt.plot(predicted, label='Predicted', color='orange', marker='x')
    plt.title(f'{model_name} Predictions vs Real Values')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    os.makedirs("plots", exist_ok=True)
    output_path = f"plots/{model_name}_predictions.png"
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"[INFO] Predictions plot saved to {output_path}")
    plt.close()


def plot_mae_evolution(mae_dict):
    """
    Affiche un graphe de l’évolution du MAE pour différents modèles.
    """
    plt.figure(figsize=(10, 5))
    names = list(mae_dict.keys())
    maes = list(mae_dict.values())
    plt.bar(names, maes, color='skyblue')
    plt.title('Mean Absolute Error by Model')
    plt.ylabel('MAE')
    plt.grid(axis='y')
    os.makedirs("plots", exist_ok=True)
    output_path = "plots/mae_evolution.png"
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"[INFO] MAE evolution plot saved to {output_path}")
    plt.close()
