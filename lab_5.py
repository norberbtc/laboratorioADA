{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPoSwXLYlWPFipwnVGgFXWw",
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
        "<a href=\"https://colab.research.google.com/github/norberbtc/laboratorioADA/blob/main/lab_5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 366
        },
        "id": "h6jBrUz8lhtX",
        "outputId": "0667593b-927c-4e85-8bbd-f388299e34f2"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-7-7dd9bff86d05>\u001b[0m in \u001b[0;36m<cell line: 35>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     34\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     35\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mjuego\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mjuego_terminado\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 36\u001b[0;31m     \u001b[0mjuego\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdibujar_mapa\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     37\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     38\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mevent\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mpygame\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mevent\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-7-7dd9bff86d05>\u001b[0m in \u001b[0;36mdibujar_mapa\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m      9\u001b[0m         \u001b[0;32mfor\u001b[0m \u001b[0mfila\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmapa\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m             \u001b[0;32mfor\u001b[0m \u001b[0mcelda\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mfila\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 11\u001b[0;31m                 \u001b[0mpygame\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdraw\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mventana\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcelda\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mmover_jugador\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtecla\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'pygame' is not defined"
          ]
        }
      ],
      "source": [
        "class Juego:\n",
        "\n",
        "    def __init__(self, mapa, inicio, fin):\n",
        "        self.mapa = mapa\n",
        "        self.inicio = inicio\n",
        "        self.fin = fin\n",
        "\n",
        "    def dibujar_mapa(self):\n",
        "        for fila in self.mapa:\n",
        "            for celda in fila:\n",
        "                pygame.draw.rect(ventana, celda, (0, 0, 0), 2)\n",
        "\n",
        "    def mover_jugador(self, tecla):\n",
        "        if tecla == pygame.K_UP:\n",
        "            self.inicio[1] -= 1\n",
        "        elif tecla == pygame.K_DOWN:\n",
        "            self.inicio[1] += 1\n",
        "        elif tecla == pygame.K_LEFT:\n",
        "            self.inicio[0] -= 1\n",
        "        elif tecla == pygame.K_RIGHT:\n",
        "            self.inicio[0] += 1\n",
        "\n",
        "    def colision(self):\n",
        "        return self.inicio == self.fin\n",
        "\n",
        "    def juego_terminado(self):\n",
        "        return self.colision()\n",
        "\n",
        "mapa = [[0, 1, 0], [1, 1, 1], [0, 0, 0]]\n",
        "inicio = [0, 0]\n",
        "fin = [2, 2]\n",
        "\n",
        "juego = Juego(mapa, inicio, fin)\n",
        "\n",
        "while not juego.juego_terminado():\n",
        "    juego.dibujar_mapa()\n",
        "\n",
        "    for event in pygame.event.get():\n",
        "        if event.type == pygame.QUIT:\n",
        "            pygame.quit()\n",
        "            quit()\n",
        "\n",
        "        if event.type == pygame.KEYDOWN:\n",
        "            juego.mover_jugador(event.key)\n",
        "\n",
        "    pygame.display.update()\n",
        "\n",
        "def leer_mapa(archivo):\n",
        "    with open(archivo, \"r\") as f:\n",
        "        filas = f.readlines()\n",
        "        dim = filas[0].split(\" \")\n",
        "        n_filas = int(dim[0])\n",
        "        n_columnas = int(dim[1])\n",
        "        mapa = []\n",
        "        for fila in filas[1:]:\n",
        "            mapa.append([int(c) for c in fila])\n",
        "        inicio = [0, 0]\n",
        "        fin = [n_filas - 1, n_columnas - 1]\n",
        "        cadena = \"\"\n",
        "        for fila in mapa:\n",
        "            cadena += \" \".join([str(c) for c in fila]) + \"\\n\"\n",
        "        cadena += f\" {inicio[0]} {inicio[1]} {fin[0]} {fin[1]}\"\n",
        "        cadena = cadena.strip()\n",
        "        return cadena\n",
        "\n",
        "path_a_mapas = \"mapas\"\n",
        "juego = JuegoArchivo(path_a_mapas)\n",
        "\n",
        "while not juego.juego_terminado():\n",
        "    juego.dibujar_mapa()\n",
        "\n",
        "    for event in pygame.event.get():\n",
        "        if event.type == pygame.QUIT:\n",
        "            pygame.quit()\n",
        "            quit()\n",
        "\n",
        "        if event.type == pygame.KEYDOWN:\n",
        "            juego.mover_jugador(event.key)\n",
        "\n",
        "    pygame.display.update()\n"
      ]
    }
  ]
}