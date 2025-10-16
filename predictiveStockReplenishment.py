{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOMB4EkoiFv3qGPZAmQw409",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/snguyenwk/projects/blob/main/predictiveStockReplenishment.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VUm0TUse8UEJ",
        "outputId": "a00a2423-e525-4c20-871b-0aaea04ccdbe"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pandas in /usr/local/lib/python3.12/dist-packages (2.2.2)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.12/dist-packages (2.0.2)\n",
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.12/dist-packages (3.10.0)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.12/dist-packages (1.6.1)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.3.3)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (0.12.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (4.60.1)\n",
            "Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.4.9)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (25.0)\n",
            "Requirement already satisfied: pillow>=8 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (11.3.0)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (3.2.5)\n",
            "Requirement already satisfied: scipy>=1.6.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn) (1.16.2)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn) (1.5.2)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn) (3.6.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n"
          ]
        }
      ],
      "source": [
        "!pip install pandas numpy matplotlib scikit-learn"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 0 : Install dependencies\n",
        "\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.ensemble import RandomForestRegressor\n",
        "from sklearn.metrics import mean_absolute_error, mean_squared_error\n",
        "import warnings\n",
        "warnings.filterwarnings(\"ignore\")\n",
        "\n",
        "np.random.seed(42)\n",
        "print(\"Environment ready. pandas:\", pd.__version__, \"numpy\", np.__version__)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fobPssjh8mH5",
        "outputId": "e851667e-a16c-4f9d-f11d-07c94002fc4b"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Environment ready. pandas: 2.2.2 numpy 2.0.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Cell 1 : Generate synthetic data\n",
        "\n"
      ],
      "metadata": {
        "id": "MZO9uHah_dnR"
      },
      "execution_count": 6,
      "outputs": []
    }
  ]
}