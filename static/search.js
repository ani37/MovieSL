const search = document.getElementById('search');
const matchlist = document.getElementById('match-list');

const searchStates = async searchText =>{
    const res = await fetch('https://data.sfgov.org/resource/yitu-d5am.json');
    const states = await res.json();

    let matches = states.filter(state => {
        const regex = new RegExp(`^${searchText}`,'gi');
        return state.title.match(regex);

    });
    if(searchText.length === 0){
        matches= [];
        matchlist.innerHTML = '';
    }
    outputHtml(matches);

};
const outputHtml = matches =>{
    if(matches.length>0){
        const html = matches.map(match => `
        <div class = "card card-body mb-1">
        <h4>${match.title} (${match.release_year})</h4>
            <small> 
            Director : <span class = "text-primary">${match.director}</span>
            | Writer : <span class = "text-primary">${match.writer} </span>
            | Production Company : <span class = "text-primary">${match.production_company}</span>
            </small>
            <small>Location: <span class = "text-primary">${match.locations}</span></small>
        </div>
        `).join('');
        matchlist.innerHTML =html;
    }
};
search.addEventListener('input',()=>searchStates(search.value));
