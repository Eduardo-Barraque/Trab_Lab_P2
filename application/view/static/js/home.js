xhr = new XMLHttpRequest();
xhr.open("GET", "/lista");
xhr.send(null);
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
    document.getElementById("Lista_Ferramentas").innerHTML = xhr.response;} 
}

function busca() {
    palavraChave = document.getElementById("Ferramentas-palavrachave").value;
    xhr = new XMLHttpRequest();
    xhr.open("GET", "/buscar?palavra_chave=" + palavraChave);
    xhr.send(null);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("Lista_Ferramentas").innerHTML = xhr.response;
        }
    }
    return false;
}

function excluir(id) {
    xhr = new XMLHttpRequest();
    xhr.open("DELETE", "remover/" + id);
    xhr.send(null);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("Lista_Ferramentas").innerHTML = xhr.response;
        }
    }
}

function editar(id){
    xhr = new XMLHttpRequest();
    xhr.open("POST", "editar/" + id);
    xhr.send(null);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("Lista_Ferramentas").innerHTML = xhr.response;
        }
    }
}

function Adicionar() {
    xhr = new XMLHttpRequest();
    xhr.open("POST", "/Adicionar");
    ferramentaHtml = document.getElementById("Criar_Tool")
    formferramenta = new FormFerramenta(ferramentaHtml);
    xhr.send(formferramenta);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("Lista_Ferramentas").innerHTML = xhr.response;
        }
}
return false;
}

function showform() {
    document.getElementById('showbutton').style.display = 'none';
    document.getElementById('Criar_Tool').style.display = 'inline-flex';
    document.getElementById('closebutton').style.display = 'flex';
  }

function closeform() {
    document.getElementById('showbutton').style.display = 'flex';
    document.getElementById('Criar_Tool').style.display = 'none';
    document.getElementById('closebutton').style.display = 'none';
}