/// <reference path="../../../source/typescript/smart.elements.d.ts" />
const data = [
                {
                    "label": 'AIPLAT',
                    "dateStart": '2021-01-10',
                    "dateEnd": '2021-09-10',
                    "class": 'product-team',
                    "type": 'task',

                },
                {
                     label: 'BIROOT',
                     dateStart: '2021-03-01',
                     dateEnd: '2021-04-30',
                     class: 'marketing-team',
                     type: 'task'
                },
                 {
                     label: 'KDL',
                     dateStart: '2021-04-11',
                     dateEnd: '2021-05-16',
                     class: 'product-team',
                     type: 'task'
                 },
                 {
                     label: 'MIRROR',
                     dateStart: '2021-05-17',
                     dateEnd: '2021-07-01',
                     class: 'dev-team',
                     type: 'task'
                 },
                 {
                     label: 'QA',
                     dateStart: '2021-07-02',
                     dateEnd: '2021-08-01',
                     class: 'design-team',
                     type: 'task'
                 },
                 {
                     label: 'IUSRTK',
                     dateStart: '2021-08-01',
                     dateEnd: '2021-09-10',
                     class: 'dev-team',
                     type: 'task'
                 },
                 {
                     label: 'Testing & QA',
                     dateStart: '2021-09-11',
                     dateEnd: '2021-10-10',
                     class: 'qa-team',
                     type: 'task'
                 },
                 {
                     label: 'UAT Test',
                     dateStart: '2021-10-12',
                     dateEnd: '2021-11-11',
                     class: 'product-team',
                     type: 'task'
                 },
                 {
                     label: 'Handover & Documentation',
                     dateStart: '2021-10-17',
                     dateEnd: '2021-11-31',
                     class: 'marketing-team',
                     type: 'task'
                 },
                 {
                     label: 'Release',
                     dateStart: '2021-11-01',
                     dateEnd: '2021-12-31',
                     class: 'release-team',
                     type: 'task'
                 }
            ];
var requestURL = 'static/gantt.json';
var request = new XMLHttpRequest();
request.open('GET', requestURL);
request.send();
request.onload = function() {
  var jsonObj = JSON.parse(request.response);
  console.log(jsonObj);
  showgantt(jsonObj);
}
function showgantt(jsonObj) {
  var heroes = jsonObj[0]['label'];
  for (var i = 0; i < heroes.length; i++) {
    var myArticle = document.createElement('article');
    var myH2 = document.createElement('h2');
    var myPara1 = document.createElement('p');
    var myPara2 = document.createElement('p');
    var myPara3 = document.createElement('p');
    var myList = document.createElement('ul');

//    myH2.textContent = heroes[i].name;
//    myPara1.textContent = 'Secret identity: ' + heroes[i].secretIdentity;
//    myPara2.textContent = 'Age: ' + heroes[i].age;
//    myPara3.textContent = 'Superpowers:';

    // var superPowers = heroes[i].powers;
    // for (var j = 0; j < superPowers.length; j++) {
    //   var listItem = document.createElement('li');
    //   listItem.textContent = superPowers[j];
    //   myList.appendChild(listItem);
    // }

    myArticle.appendChild(myH2);
    myArticle.appendChild(myPara1);
    myArticle.appendChild(myPara2);
    myArticle.appendChild(myPara3);
    myArticle.appendChild(myList);

//    section.appendChild(myArticle);
  }
}

window.Smart("#gantt", class {
    get properties() {
        return {
            treeSize: '20%',
            durationUnit: 'hour',
            taskColumns: [
                {
                    label: 'Задача',
                    value: 'label',
                    size: '60%'
                },
                {
                    label: 'Количество часов',
                    value: 'duration',
                    formatFunction: (date) => parseInt(date)
                }
            ],
            dataSource: data
        };
    }
});
export {};