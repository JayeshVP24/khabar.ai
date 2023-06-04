var urlRegex = /(https?:\/\/[^\s]+)/g;
const BACKEND_URL = "http://0.0.0.0:5000";
const HEADER = {
  "Access-Control-Allow-Origin": "*",
  Accept: "*/*",
};

class UrlLinks {
    /**
     *
     * @param {string} input
     * @returns {string}
     */
    static urlFromMsg = (input) => {
      const url = input.match(urlRegex);
      if (url !== null) {
        return url[0];
      }
      return null;
    };


    /**
   *
   * @param {string} url
   * @returns {string}
   */
  static summary = async (url) => {
    const uri = new URL(BACKEND_URL);
    uri.pathname = "/summary";
    uri.searchParams.append("url", url);
    console.log(uri.toString());
    try {
      const res = await fetch(uri.toString(), {
        headers: HEADER,
      });
      const data = await res.json();
      console.log("data ", data.result);
      return data.result;
    } catch {
      console.log("error");
      return "error";
    }
  };

  /**
   * 
   * @param {string} url 
   * @returns {string}
   */
  static hatespeech = async (url) => {

  }
/**
 * 
 * @param {string} url
 * @returns {{
 *  likecount: number,
 * retweet: number,
 * hashtags: string[],
 * count: number,
 * }}
 */
  static twitterAnalysis = async (url) => {
    const uri = new URL(BACKEND_URL);
    uri.pathname = "/twitter";
    uri.searchParams.append("query", url);
    console.log(uri.toString());
    try {
      const res = await fetch(uri.toString(), {
        headers: HEADER,
      });
      const data = await res.json();
      console.log("data ", data.result);
      return data.result;
    } catch {
      console.log("error");
      return "error";
    }
  }
/**
 * 
 * @param {string} url 
 * @returns {{
 *  bots: string[],
 * flag: boolean
 * } | string}
 */
  static botAcivity = async (url) => {
    const uri = new URL(BACKEND_URL);
    uri.pathname = "/twitter";
    uri.searchParams.append("url", url);
    console.log(uri.toString());
    try {
        const res = await fetch(uri.toString(), {
          headers: HEADER,
        });
        const data = await res.json();
        console.log("data ", data);
        return data;
      } catch {
        console.log("error");
        return "error";
      }
  }
/**
 * 
 * @param {string} url 
 * @returns {{
 * authentic: boolean} | string}
 */
  static authenticity = async (url) => {
    const uri = new URL(BACKEND_URL);
    uri.pathname = "/authenticity";
    uri.searchParams.append("url", url);
    console.log(uri.toString());
    try {
        const res = await fetch(uri.toString(), {
          headers: HEADER,
        });
        const data = await res.json();
        console.log("data ", data);
        return data;
      } catch {
        console.log("error");
        return "error";
      }
  }  

//   need  to send image here
  static propogandaCheck = async (url) => {
    const uri = new URL(BACKEND_URL);
    uri.pathname = "/propaganda";
    uri.searchParams.append("url", url);
    console.log(uri.toString());
    try {
        const res = await fetch(uri.toString(), {
          headers: HEADER,
        });
        const data = await res.json();
        console.log("data ", data);
        return data.data;
      } catch {
        console.log("error");
        return "error";
      }
  }

/**
 * 
 * @param {string} url 
 * @returns {string}
 */
  static twitterSentiment = async (url) => {
    const uri = new URL(BACKEND_URL);
    uri.pathname = "/sentiment";
    uri.searchParams.append("query", url);
    console.log(uri.toString());
    try {
        const res = await fetch(uri.toString(), {
          headers: HEADER,
        });
        const data = await res.json();
        console.log("data ", data);
        return data.data;
      } catch {
        console.log("error");
        return "error";
      }
  }
/**
 * 
 * @param {string} url 
 * @returns {BlobPart}
 */
  static wordcloud = async (url) => {
    const uri = new URL(BACKEND_URL);
    uri.pathname = "/cloud2";
    uri.searchParams.append("url", url);
    console.log(uri.toString());
    try {
        const res = await fetch(uri.toString(), {
          headers: HEADER,
        });
        const data = await res.blob();
        return data
      } catch {
        console.log("error");
        return "error";
      }
  }

}

module.exports = { UrlLinks };
