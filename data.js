const proyectos = [
   {
  titulo: "Ajedrez 3D con Three.js - TMChess3D",
  descripcion: "Implementación interactiva de un juego de ajedrez en 3D utilizando Three.js, con movimientos válidos, animaciones, rotación de cámara y selección de piezas.",
  link: "https://bc5d5c14ef21.ngrok-free.app/chess.html",
  fecha: "01/12/2023",
  imagen: "3.png",
  tecnologias: ["Three.js", "JavaScript", "WebGL", "HTML5", "CSS3", "3D Modeling", "Animación 3D"]
},
  {
    titulo: "Pong",
    descripcion:
      "Creación de un juego sencillo estilo Pong.",
    link: "https://miguecg02.github.io/Pong",
    fecha: "29/03/2023",
    imagen: "4.png",
    tecnologias: ["Javascript"],
  },
  {
    titulo: "Miguel responde",
    descripcion:
      "Juego para hacer creer a la gente de que hay una inteligencia artificial que sabe todo sobre tí.",
    link: "https://miguecg02.github.io/Miguel-Responde/",
    fecha: "29/02/2023",
    imagen: "6.png",
    tecnologias: ["HTML","CSS","Javascript"],
  },
  {
    titulo: "Test de mecanografía",
    descripcion:
      "Juego para ver quién puede escribir más rápido. Se te da un minuto y tenés que escribir la mayor cantidad de letras correctas evitando escribir letras incorrectas.",
    link: "https://miguecg02.github.io/test-mecanografia/",
    fecha: "29/02/2023",
    imagen: "5.png",
    tecnologias: ["HTML","CSS","Javascript","APIs"],
  },
 {
  titulo: "Agenda de contactos",
  descripcion: "Agenda de contactos ejemplo. Versión 2025. Proyecto generado con Angular CLI version 19.0.0 y actualizado a Angular 20.2.",
  link: "https://github.com/miguecg02/Agenda-contactos/tree/gh-pages/src", // Enlace directo a los archivos
  fecha: "29/02/2023",
  imagen: "8.png",
  tecnologias: ["Angular","SCSS","Typecript", "HTML" ,"APIs"],
},
  {
  titulo: "Contador de truco",
  descripcion:
    "Herramienta para contar puntos en el juego de truco.",
  link: "https://miguecg02.github.io/Contador-Truco/", // demo funcionando
  fecha: "18/09/2025",
  imagen: "2.png",
  tecnologias: ["HTML","CSS","Javascript"],
},
  {
    titulo: "Ruelta personalizable",
    descripcion:
      "Herramienta para generar un sorteo entre opciones y visualizarlo como si fuese una ruleta. Para practicar eventos y para demostrar el uso que puede tener la matemática en un proyecto.",
    link: "https://miguecg02.github.io/Ruleta/",
    fecha: "08/02/2023",
    imagen: "9.png",
    tecnologias: ["HTML", "CSS", "Javascript"],
  },
  {
    titulo: "Herramienta para un 'amigo invisible'",
    descripcion:
      "Herramienta que nos permite gestionar varios sorteos de amigos invisibles (una actividad en donde se hacen regalos entre grupos de amigos). Está creada pensada en su eso en teléfonos.",
    link: "https://amigo-inivisible.netlify.app/",
    fecha: "08/02/2023",
    imagen: "invisible.png",
    tecnologias: ["Angular", "Ionic", "Typescript"],
  },
  {
    titulo: "Programa de realidad aumentada'",
    descripcion:
      "Este program nos permite mediante códigos Aruco ver modelos 3D en realidad aumentada Dentro del repositorio estará toda la documentación del proyecto.",
    link: "https://github.com/miguecg02/CUIA",
    fecha: "08/02/2023",
    imagen: "11.png",
    tecnologias: ["CSS", "HTML", "Javascript"],
  }

  
];

const informacionPersonal = {
  nombre: "Miguel Ángel Caballero Gómez ",
  subtitulo: "Desarrollador de software",
  imagen: "img/migue1.png",
  otros: [
    ["Nacionalidad", "Español"],
    [
      "Edad",
      new Date(new Date() - new Date("2002/02/07")).getFullYear()-1970 + " años",
    ],
  ],
  idiomas: [
    ["Español", "Nativo"],["Inglés", "Muy bueno"],["Portugués", "Bueno"],
  ],
  tecnologias: [
    ["Html", 9],["Css", 8],["Javascript", 9],["Typescript", 8],["Angular", 9],
    ["Ionic",7],["Node",6],["Python",5],["C#",3]
  ]
};
