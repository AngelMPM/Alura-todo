<canvas width="600" height="400"> </canvas>

var pantalla = document.querySelector("canvas");
  var pincel = pantalla.getContext("2d");

    function dibujarBarra(x, y, serie, colores, texto) {
        var pantalla = document.querySelector("canvas");
        var pincel = pantalla.getContext("2d");

        // Calcular el ancho de cada rectángulo en función del ancho total del gráfico
        var anchoRectangulo = (pantalla.width - x) / serie.length;

        // Escribir el texto del año en la parte superior de la barra
        escribirTexto(x, y - 20, texto);

        // Dibujar los rectángulos de la barra
        var alturaAcumulada = y;
        for (var i = 0; i < serie.length; i++) {
            var alturaRectangulo = serie[i] / 100 * (pantalla.height - y);
            dibujarRectangulo(x, alturaAcumulada, anchoRectangulo, alturaRectangulo, colores[i]);
            alturaAcumulada += alturaRectangulo;
        }
    }
    dibujarBarra(50, 50, serie2009, colores, "2009");
    dibujarBarra(150, 50, serie2019, colores, "2019");
