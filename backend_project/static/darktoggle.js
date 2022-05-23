/* Own darkmode worked, but didn't use 'toggle' method. Couldn't get
   own toggle darkmode working, so integrate lecturer example instead. */

//do this one first

// function darkmode() {
//     let element = document.body;
//     element.classList.toggle("dark-mode");
// }

// dont forget to add the css, and the onclick event

// The other two big classes we have are main box - the white box, and main Text, the text inside it! So I think we should change them too - so I'll write some CSS for them, and by that I mean uncomment the CSS out I have here. And then we'll define them a bit more in JS. So to select all instances of an element we can use getElementsbyClassName. I want to refer to all these elements so I'll write:

function darkmode() {

    let elementb = document.body;
    let list = document.getElementsByClassName("main-box"); // all the examples will get saved in a list
    let listb = document.getElementsByClassName("main-text");
    let state = localStorage.getItem("state") //** */ save this line for later - here, I'm getting the key, and saving the value of that key to a variable

    elementb.classList.toggle("dark-mode"); //so I'll keep my toggle

    for (const element of list) {  // and then I'll use a for loop - for each thing in the list, toggle darkmode
        element.classList.toggle('dark-modeb');
    }

    for (const element of listb) {
        element.classList.toggle('dark-mode'); // so let's give this a try! Look! That works - it's not perfect but now we know, it works!
    }

    // the first thing we need to know about is localStorage - it allows us to store data as an object in a browser. It saves this data as key/value pairs.
    // so I want some logic here - I want like a light switch. I want to say if dark mode is on, give me a value called dark, and if dark mode isn't on, give me a value called light. 

    if (state !== "dark") {
        localStorage.setItem("state", "dark") // this line is making that local storage item - set the item to have a key of state and a value of dark
    } else {
        localStorage.setItem("state", "light") // and do the opposite so now I need to actuall make that variable state! - go to the ** line 19
    }
}

//remember to put onbody load
function darkCheck() {

    let elementb = document.body;
    let list = document.getElementsByClassName("main-box");
    let listb = document.getElementsByClassName("main-text");
    let state = localStorage.getItem("state")

    if (state == "dark") {
        elementb.classList.toggle("dark-mode");

        for (const element of list) {
            element.classList.toggle('dark-modeb');
        }

        for (const element of listb) {
            element.classList.toggle('dark-mode');
        }
    }
}

/* only one onload event per body, so
   redirect to here and run both startups */
function doDarkCookies() { checkCookies();  darkCheck(); }