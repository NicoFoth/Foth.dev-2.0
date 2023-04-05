var age, daysBetweenDates;
daysBetweenDates = function(d1, d2) {
  var diffDays, oneDay;
  oneDay = 24 * 60 * 60 * 1000;
  diffDays = (d2 - Date.parse(d1)) / oneDay;
  return diffDays;
};

age = function() {
    document.getElementById("age").innerHTML = (daysBetweenDates('Sep 3, 2002 00:00:00', new Date()) / 365);
}

setInterval(age, 100)


const firstContent = "2013 wurde ich in die Inselschule Fehmarn eingeschult. Die Inselschule Fehmarn ist eine Gemeinschaftsschule an der Ostsee. Eine Gemeinschaftsschule verbindet alle drei Bildungsgrade miteinander. Man arbeitet in einer Klasse auf Hauptschul-, Realschul- und Abiturniveau.";
const secondContent= "In der 10. Klasse war ich dann zu Besuch bei Actian in Hamburg. Actian ist ein Softwareentwicklungsunternehmen, welches sich auf hybrides Datenmanagement und die Analyse derer spezialisiert. Dort hatte ich die Möglichkeit als Praktikant einen Einblick in viele Bereiche des Unternehmens zu erlangen und an dem Eclipse Plugin für die Versant JPA (Java Persistence API) zu arbeiten.";
const thirdContent = "In der 11. Klasse war ich dann wieder bei Actian. Dieses Mal habe ich dort Recherche für einen Entitlement Service für Salesforce, Zwecks des neues Avalanche Produkts betrieben. Ziel war es das Beste webservice Framework und die dazugehörige Sprache zu finden. Meine Ergebnisse trug ich zusammen und stellte die jeweiligen Vorteile, Nachteile und meine Empfehlung in einem Meeting dem Entwickler- und QA-Team vor.";
const fourthContent = "Im Juni 2022 werde ich voraussichtlich mein Abitur an der Inselschule Fehmarn absolvieren. Meine Pläne sind ein duales Studium in der angewandten Informatik in der Umgebung Hamburg oder Kiel zu beginnen. Wie sich dies dann allerdings genauer gestaltet, steht noch in den Sternen.";


function changeToFirst() {
    document.getElementById("timeline-content").innerHTML = firstContent;
    document.getElementById("timeline-dot-1").classList.remove("timeline-dot-lowlight");
    document.getElementById("timeline-dot-2").classList.add("timeline-dot-lowlight");
    document.getElementById("timeline-dot-3").classList.add("timeline-dot-lowlight");
    document.getElementById("timeline-dot-4").classList.add("timeline-dot-lowlight");

    document.getElementById("timeline-text-1").style.color = "white";
    document.getElementById("timeline-text-2").style.color = "grey";
    document.getElementById("timeline-text-3").style.color = "grey";
    document.getElementById("timeline-text-4").style.color = "grey";
    }

function changeToSecond() {
    document.getElementById("timeline-content").innerHTML = secondContent;
    document.getElementById("timeline-dot-2").classList.remove("timeline-dot-lowlight");
    document.getElementById("timeline-dot-1").classList.add("timeline-dot-lowlight");
    document.getElementById("timeline-dot-3").classList.add("timeline-dot-lowlight");
    document.getElementById("timeline-dot-4").classList.add("timeline-dot-lowlight");

    document.getElementById("timeline-text-2").style.color = "white";
    document.getElementById("timeline-text-1").style.color = "grey";
    document.getElementById("timeline-text-3").style.color = "grey";
    document.getElementById("timeline-text-4").style.color = "grey";
    }

function changeToThird() {
    document.getElementById("timeline-content").innerHTML = thirdContent;
    document.getElementById("timeline-dot-3").classList.remove("timeline-dot-lowlight");
    document.getElementById("timeline-dot-1").classList.add("timeline-dot-lowlight");
    document.getElementById("timeline-dot-2").classList.add("timeline-dot-lowlight");
    document.getElementById("timeline-dot-4").classList.add("timeline-dot-lowlight");

    document.getElementById("timeline-text-3").style.color = "white";
    document.getElementById("timeline-text-1").style.color = "grey";
    document.getElementById("timeline-text-2").style.color = "grey";
    document.getElementById("timeline-text-4").style.color = "grey";
    }

function changeToFourth() {
    document.getElementById("timeline-content").innerHTML = fourthContent;
    document.getElementById("timeline-dot-4").classList.remove("timeline-dot-lowlight");
    document.getElementById("timeline-dot-1").classList.add("timeline-dot-lowlight");
    document.getElementById("timeline-dot-2").classList.add("timeline-dot-lowlight");
    document.getElementById("timeline-dot-3").classList.add("timeline-dot-lowlight");

    document.getElementById("timeline-text-4").style.color = "white";
    document.getElementById("timeline-text-1").style.color = "grey";
    document.getElementById("timeline-text-2").style.color = "grey";
    document.getElementById("timeline-text-3").style.color = "grey";
    }
