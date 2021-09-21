<template>
  <div class="App">
      <div id="logo">
        <svg>
          <g fill="none" fill-rule="evenodd">
            <path 
              d="M73.788 15.395v11.772h-4.95V16.414c0-2.528-1.624-4.075-3.702-4.075-2.645 0-4.383 1.811-4.383 5.773v9.055h-4.988V16.414c0-2.528-1.625-4.075-3.703-4.075-2.645 0-4.307 1.811-4.307 5.773v9.055h-4.988V8.34h4.988v1.547c1.322-1.32 3.173-2.113 5.63-2.113 2.531 0 4.836 1.094 6.196 3.094 1.55-1.924 3.854-3.094 6.877-3.094 3.93 0 7.33 3.019 7.33 7.622zm3.588 11.772V8.34h4.987v18.828h-4.987zm0-22.186V.001h4.987v4.98h-4.987zm27.506 10.716v11.47h-4.987V16.753c0-2.64-1.512-4.414-3.816-4.414-2.834 0-4.686 1.886-4.686 6.49v8.338h-4.987V8.34h4.987v1.698c1.474-1.472 3.439-2.264 5.933-2.264 4.534 0 7.556 3.245 7.556 7.924zm17.267 2.075c0-3.471-2.683-5.66-5.365-5.66-3.023 0-5.29 2.189-5.29 5.66 0 3.472 2.267 5.622 5.29 5.622 2.682 0 5.365-2.15 5.365-5.622zm4.988 9.395h-4.988v-1.471c-1.587 1.283-3.665 2.038-6.234 2.038-4.8 0-9.258-4.038-9.258-9.962 0-5.924 4.459-9.999 9.258-9.999 2.569 0 4.647.755 6.234 2.075V0h4.988v27.167zm7.366-11.583h9.107c-.643-2.415-2.457-3.472-4.46-3.472-1.888 0-4.042 1.132-4.647 3.472zm14.208 3.51h-14.359c.492 2.716 2.419 4.376 4.723 4.376 1.474 0 3.325-.189 4.686-2.49l4.458.943c-1.662 3.924-5.025 5.81-9.144 5.81-5.327 0-9.672-4.037-9.672-9.96 0-5.925 4.345-10 9.748-10 5.025 0 9.37 3.886 9.56 9.622v1.698zm7.082-3.51h9.106c-.642-2.415-2.456-3.472-4.458-3.472-1.89 0-4.044 1.132-4.648 3.472zM170 19.094h-14.358c.491 2.716 2.418 4.376 4.723 4.376 1.473 0 3.325-.189 4.685-2.49l4.459.943c-1.663 3.924-5.026 5.81-9.144 5.81-5.328 0-9.673-4.037-9.673-9.96 0-5.925 4.345-10 9.749-10 5.025 0 9.37 3.886 9.559 9.622v1.698z" 
              fill="#001E3C">
            </path>
            <path 
              d="M18.329 0h13.746v32H18.33V27.43h9.164V4.572H18.33V0zM4.582 13.714V27.43h9.165V32H0V0h13.747v4.571H4.582v9.143zm4.582 0v-4.57h13.747v4.57H9.164zm0 9.143v-4.571h4.583v4.571H9.164z" 
              fill="#FD3246">
            </path>
          </g>
        </svg>
      </div>
      <div class="container">
        <div class="content">
          <h1>Mindee case</h1>
          <br />
          <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
          <div v-for="family_index, family in ocr" v-bind:key="family_index">
            <p class="family">{{ family }}</p>
            <p class="element" v-for="element, index in family_index" v-bind:key="index">{{ index }} : {{ element }}</p>
          </div>
        </div>
      </div>
      <div class="container gray">
        <span>
          <img src="" id="photo" alt="photo" />
        </span>
      </div>
    </div>
</template>

<script>
  import axios from "axios";
  export default {
    data(){
      return {
        file: '',
        ocr: ''
      }
    },
    methods: {
      submitFile(){
        let formData = new FormData();
        
        formData.append('file', this.file);

        axios.post(this.$hostname + '/image_parsing',
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        ).then((response) => {
          this.ocr = response.data;
        })
        .catch(error => {
          console.log(error)
        });
      },
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
        this.submitFile();
      }
    }
  }
</script>

<style>
  @font-face {
      font-family: "Eina02";
      src: local("Eina02-Bold"),
      url("../Eina02-Bold.ttf") format("truetype");
      font-weight: bold;
  }

  body {
      height: 100%;
      position: absolute;
      margin: 0;
      color: #001e3c;
      font-family: Eina02;
      font-weight: 400!important;
  }

  h1 {
      display: initial;
      border-bottom: solid 2px #FD3246;
  }

  span {
      text-align: center;
      width: 100%;
  }

  #app {
      height: 100%;
      width: 100%;
      position: fixed;
  }

  #logo {
      position: absolute;
      top: 20px;
      left: 20px;
  }

  #photo {
      position: relative;
      width: 90%;
  }

  #ocr {
      z-index: 1000;
      position: absolute;
  }

  .App {
      height: 100%;
      display: flex;
  }

  .container {
      display: flex;
      align-items: center;
      width: 50%;
  }

  .content {
      text-align: center;
      width: -webkit-fill-available;
  }

  .gray {
      background-color: lightgray;
  }

  .element {
    background: lightgray;
    display: block;
    padding: 3px;
    border-radius: 5px;
    width: fit-content;
    text-align: center;
    margin: auto;
    margin-top: 10px;
    margin-bottom: 10px;
  }

  .family {
    width: -webkit-fit-content;
    width: -moz-fit-content;
    width: fit-content;
    margin: auto;
    margin-bottom: 25px;
    margin-top: 25px;
    border-bottom: solid 2px #FD3246;
  }
</style>