/**
 * Estilos de el popover
 * @type {Object}
 */
const styles = {
  "[popover]": `box-sizing: border-box;background-color: #0C157999;padding: 1vh 2vw;border-radius: 10px`,
  "[popover] .header-banner": `display: flex;align-items: center;justify-content: center;width: 100%;margin: 0;`,
  "[popover] .btn-container": `display: flex;width: 170%;justify-content: flex-end;`,
  "[popover] .btn-toggle": `transform: translate(1vh, -2vh);border-radius: 5px 0 0 5pc;border: none;padding: 3vw;color: #FFFFFF;max-height: 6vh;background-color: #00053C;`,
  "[popover] .spn-pop-ouo": `display: block;transform: translate(1vw, .5vh);font-size: 3vh;`,
  "[popover] .body-banner": `display: flex;justify-content: center;`,
  "[popover] .img-banner": `width: 70vw;border-radius: 20px`,
};

/**
 * Popover, contenedor
 * @type {HTMLElement}
 */
const html = `
      <div class="banner" id="banner-ouo" popover="manual" data-popover="ouo-refer">
          <header class="header-banner">
            <div class="btn-container">
              <button title="Close" class="btn-toggle" id="__close"><span class="spn-pop-ouo"></span></button>
            </div>
          </header>
          <section class="body-banner">
            <!-- Start of ouo.io banner code -->
            <a href="http://ouo.io/ref/hoidZ1Y5"><img class="img-banner" src="http://ouo.io/images/banners/r5.jpg" title="ouo.io - Make short links and earn the biggest money" /></a>
            <!-- End of ouo.io banner code -->
          </section>
      </div>`;

/**
 * Popover con imagen de ouo.io referral
 */
export default class PopOuo {
  /**
   * Popover elemento
   * @type {HTMLElement}
   */
  pop;
  constructor() {
    // Cargar contenido (popover)
    this.load();
    // Contenedor popover
    this.pop = document.querySelector('[data-popover="ouo-refer"]');
    document.querySelector("#btn-tog").click();
  }

  load() {
    document.body.insertAdjacentHTML("beforeend", html);
    // this.stylesLoad();
    this.listenClose();
  }

  stylesLoad() {
    /**
     * @type {HTMLStyleElement}
     */
    // const tag_style = document.createElement("style");
    // for (let style in styles) {
    //   tag_style.innerHTML += `${style}{${styles[style]}}\n`;
    // }
    const tag_style = "";

    document.head.insertAdjacentElement("beforeend", tag_style);
  }

  listenClose() {
    const btn_close = document.querySelector("#__close");
    btn_close.addEventListener("click", (e) => {
      e.preventDefault();
      this.pop.hidePopover();
    });
  }
}

/*
      
      [popover] {
      
            box-sizing: border-box;
      
            background-color: #0C157999;
      
            padding: 1vh 2vw;
      
            border-radius: 10px
      
          }
      
          [popover]:popover-open {
      
            display: block
      
          }
      
          [popover] .header-banner {
      
            display: flex;
      
            align-items: center;
      
            justify-content: center;
      
            width: 100%;
      
            margin: 0;
      
          }
      
          [popover] .btn-container {
      
            display: flex;
      
            width: 170%;
      
            justify-content: flex-end;
      
          }
      
          
      
          [popover] .btn-toggle{
      
            transform: translate(1vh, -2vh);
      
            border-radius: 5px 0 0 5pc;
      
            border: none;
      
            padding: 3vw;
      
            color: #FFFFFF;
      
            max-height: 6vh;
      
            background-color: #00053C;
      
          }
      
          
      
          [popover] .spn-pop-ouo{
      
            display: block;
      
            transform: translate(1vw, .5vh);
      
            font-size: 3vh
      
          }
      
          [popover] .body-banner {
      
            display: flex;
      
            justify-content: center;
      
          }
      
          [popover] .img-banner {
      
            width: 70vw;
      
            border-radius: 20px
      
          }
      
      */

new PopOuo();
