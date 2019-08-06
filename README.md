Instructions - 

Step1: Fork & clone the git repository
git clone <URL>

Step2: Install & start the docker desktop

Step3: Go to cloned directory
cd test1111

Step4: Build the docker image
docker build -t summarizer-api .

Step5: Run a container instance
docker run -p 5000:5000 summarizer-api

Step6: Open a browser & type http://0.0.0.0:5000/

Step5: Test some sample URLs like below. URLs should be publicly scrapable.

https://www.barrons.com/articles/ibm-is-a-growth-stock-again-thanks-to-red-hat-acquisition-51565025034 
https://www.moneycontrol.com/news/business/infosys-sets-up-cyber-defence-centre-in-bucharest-4259681.html?classic=true
https://www.cips.org/en/supply-management/news/2019/august/extra-brexit-border-funding-not-enough/
