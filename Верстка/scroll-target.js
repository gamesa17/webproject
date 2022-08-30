class scrollField{
    scrollField;
    scrollFieldOffset;
    scrollFieldHeight;;

    scrollBody;
    scrollBodyHeight;

    constructor(scrollField){
        this.scrollField = scrollField;
    }

    initFieldParams() {
        this.scrollFieldOffset = this.scrollField.offsetTop;
        this.scrollFieldHeight = this.scrollField.scrollHeight;
        this.scrollBody = this.scrollField.querySelector('.scroll-body');
        this.scrollBodyHeight = this.scrollBody.scrollHeight;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    docElement = document.documentElement;
    scrollFieldDOM = document.querySelectorAll('.scroll-field');
    let scrollFieldArray = [scrollFieldDOM.length];
    scrollFieldDOM.forEach(function(field, a, arr){
        scrollFieldArray[a] = new scrollField(field);
        scrollFieldArray[a].initFieldParams();
        console.log(scrollFieldArray[a]);
    })

    ///ADD RESIZE EVENT 

    window.addEventListener('scroll', () =>{
        scrollFieldArray.forEach( function(field, a, arr){
            if((field.scrollFieldOffset < (window.pageYOffset + docElement.clientHeight)) && ((field.scrollFieldOffset + field.scrollFieldHeight) > window.pageYOffset)){
                scrollElements = field.scrollBody.querySelectorAll('.scroll-element');
                scrollElements.forEach( element => {
                    // console.log(Math.floor(( scrollBody[a].offsetTop - fieldPositionList[a]) / (fieldHeightList[a] - scrollBody[a].scrollHeight) * 100));
                    var scrollStart = parseFloat(element.style.getPropertyValue("--scroll-start"));
                    var scrollEnd = parseFloat(element.style.getPropertyValue("--scroll-end"));
                    var wayFract = Math.floor((field.scrollBody.offsetTop - field.scrollFieldOffset) / (field.scrollFieldHeight - document.documentElement.clientHeight) * 100);
                    console.log(wayFract);
                    if( scrollStart <= wayFract && scrollEnd > wayFract){
                        element.classList.remove("scroll-element-after");
                        element.classList.remove("scroll-element-before");
                        // element.style.top = (Math.max(0, 100 * (1 - ((wayFract - elementFract) / (elementFract + 0.1))))) + "vh";
                        element.classList.add("scroll-element-activate");
                        // if(element.classList.contains("scroll-element-skipped")){
                        // }
                        console.log("yes");
                    }
                    if(scrollEnd <= wayFract && scrollStart < wayFract){
                        element.classList.add("scroll-element-after");
                        element.classList.remove("scroll-element-activate");
                        console.log("no");
                    }
                    if(scrollStart > wayFract){
                        element.classList.remove("scroll-element-activate");
                        element.classList.add("scroll-element-before");
                        console.log("maybe")
                    }
                })
            }
        });
    })
}, false);
 
console.log(document.getElementById('scroll1'));
document.getElementById('scroll1').onscroll = function(){
    // console.log(window.pageYOffset);
};
