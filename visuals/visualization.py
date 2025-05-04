import matplotlib.pyplot as plt


def plot_predictions(real, predicted, model_name='Model'):
    """
    Affiche un graphe des vraies valeurs vs. les prédictions.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(real, label='Real', color='blue')
    plt.plot(predicted, label='Predicted', color='orange')
    plt.title(f'{model_name} Predictions vs Real Values')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


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
    plt.tight_layout()
    plt.show()
