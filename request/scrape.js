// Define the URL of the website you want to scrape
const url = "https://hidemy.io/en/proxy-list/?type=hs#list";

fetch(url)
  .then(response => response.text())
  .then(html => {
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = html;

    const trElements = tempDiv.querySelectorAll("tr");
    for (let i = 1; i < trElements.length; i++) {
      const tdElements = trElements[i].querySelectorAll("td");

      if (tdElements.length >= 2) {
        const firstText = tdElements[0].textContent.trim();
        const secondText = tdElements[1].textContent.trim();
        console.log(`${firstText}:${secondText}`);
      }
    }
  })
  .catch(error => {
    console.error("Failed to retrieve the webpage:", error);
  });
