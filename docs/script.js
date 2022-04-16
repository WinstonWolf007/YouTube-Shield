//////////////////////////////////////////////////////////////
// the head bar
//////////////////////////////////////////////////////////////

let bar = document.getElementById('front')

window.onscroll = function() {func()};

function func()
{
    let scroll_num = document.documentElement.scrollTop;
    let heigth1 = window.innerHeight * scroll_num / 2461
    let heigth2 = heigth1 * 100 / window.innerHeight
    bar.style.width = heigth2 + '%'
}

// scrool max => 2461
// windows height => 968

// document.body.onscroll = function( event ) {
//     console.log(document.body.scrollTop)
// };


//////////////////////////////////////////////////////////////
// the code box
//////////////////////////////////////////////////////////////

let box = document.querySelectorAll('.code')
let colors = {
    'r': '#FF9680',
    'g': '#80FF91',
    'b': '#80BDFF',
    'p': '#FF80C8',
    'w': '#fff',
    'y': '#FFE880',
    'grey': '#777'
}

function check(keyword, lists) {
    for (let i=0; i<lists.length; i++) {
        if (lists[i] == keyword) {
            return true
        }
    }
    return false
}

function isdigit(num) {
    return !isNaN(num);
}

saveLine = false
inString = false

for (let each_box=0; each_box<box.length; each_box++)
{
    let txt = box[each_box].innerHTML.split('\\n');
    for (let line=0; line<txt.length; line++)
    {
        let txt_line = txt[line].split(' ');

        for (let word=0; word<txt_line.length; word++)
        {
            let keyword = txt_line[word].replace('\n', '').replace('\\t', '');
            if (check(keyword, ['if', 'else:', 'elif', 'for', 'while', 'def', 'class', 'import', 'from', 'return', 'pass'])) {
                txt_line[word] = '<span style="color: ' + colors['b'] + ';"><strong>' + txt_line[word] + '</strong></span>';
            }
            else if (keyword[0] == '@') {
                txt_line[word] = '<span style="color: ' + colors['y'] + ';"><strong>' + txt_line[word] + '</strong></span>';
            }
            else if (keyword[0] == '#') {
                txt[line] = '<span style="color: ' + colors['grey'] + ';">' + txt_line.join(' ') + '</span>';
                saveLine = true;
                break;
            }
            else if (isdigit(keyword)) {
                txt_line[word] = '<span style="color: ' + colors['g'] + ';">' + keyword + '</span>';
            }
        }
        if (!saveLine) {
            txt[line] = txt_line.join(' ');
        }
        else {
            saveLine = false;
        }
        
    }
    txt = txt.join('<br>')

    for (let f=0; f<txt.length; f++)
    {
        txt = txt.replace("\\t", '&nbsp;&nbsp;&nbsp;&nbsp;')
    }
    
    box[each_box].innerHTML = txt
}
