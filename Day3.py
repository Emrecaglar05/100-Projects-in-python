{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5yV2T2iMNYJ2",
        "outputId": "3629297a-3621-4895-d6f8-4a353e9e6f64"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your name Emre\n",
            "Hello,  Emre!\n"
          ]
        }
      ],
      "source": [
        "name = input(\"Enter your name\")\n",
        "print(f\"Hello, {name}!\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num1 = input(\"Enter a number\")\n",
        "num1 = str(num1)\n",
        "print(f\"Number doubled: {num1 * 2}\")\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eryGiRN1N4Ca",
        "outputId": "f52e074c-6b9b-443d-c28e-0f500c1cacd0"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number10\n",
            "Number doubled: 1010\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "number1 = float(input(\"Enter a number\"))\n",
        "number2 = float(input(\"Enter a number\"))\n",
        "\n",
        "addition = number1 + number2\n",
        "subtraction = number1 - number2\n",
        "multiplication = number1 * number2\n",
        "division = number1 / number2\n",
        "print()\n",
        "print(f\"Addition: {number1} + {number2} = {addition}\")\n",
        "print(f\"Subtraction: {number1} - {number2} = {subtraction}\")\n",
        "print(f\"Multiplication: {number1} * {number2} = {multiplication}\")\n",
        "print(f\"Division: {number1} / {number2} = {division}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3sIfTXAzPXm5",
        "outputId": "20c4dcb7-d4d0-4285-e17f-10ee5ceea74d"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number 10\n",
            "Enter a number 2\n",
            "Addition: 10.0 + 2.0 = 12.0\n",
            "Subtraction: 10.0 - 2.0 = 8.0\n",
            "Multiplication: 10.0 * 2.0 = 20.0\n",
            "Division: 10.0 / 2.0 = 5.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"------------Welcome To My Calculator------------\")\n",
        "\n",
        "choice = input(\"Please select a calculation type (a/s/m/d/mo/ex): \")\n",
        "\n",
        "if choice in [\"a\", \"s\", \"m\", \"d\", \"mo\", \"ex\"]:\n",
        "    number1 = int(input(\"Enter a number: \"))\n",
        "    number2 = int(input(\"Enter a second number: \"))\n",
        "\n",
        "    if choice == \"a\":\n",
        "        print(f\"Addition: {number1} + {number2} = {number1 + number2}\")\n",
        "    elif choice == \"s\":\n",
        "        print(f\"Subtraction: {number1} - {number2} = {number1 - number2}\")\n",
        "    elif choice == \"m\":\n",
        "        print(f\"Multiplication: {number1} * {number2} = {number1 * number2}\")\n",
        "    elif choice == \"d\":\n",
        "        if number2 != 0:\n",
        "            print(f\"Division: {number1} / {number2} = {number1 / number2}\")\n",
        "        else:\n",
        "            print(\"Error: Division by zero is not allowed.\")\n",
        "    elif choice == \"mo\":\n",
        "        print(f\"Modulus: {number1} % {number2} = {number1 % number2}\")\n",
        "    elif choice == \"ex\":\n",
        "        print(f\"Exponentiation: {number1} ** {number2} = {number1 ** number2}\")\n",
        "else:\n",
        "    print(\"Invalid choice. Please try again.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3lGoMuf0QY7L",
        "outputId": "02bf3fac-0303-43dd-8dfe-fdab889eb4dd"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "------------Welcome To My Calculator------------\n",
            "Please select a calculation type (a/s/m/d/mo/ex): ex\n",
            "Enter a number: 12\n",
            "Enter a second number: 5\n",
            "Exponentiation: 12 ** 5 = 248832\n"
          ]
        }
      ]
    }
  ]
}