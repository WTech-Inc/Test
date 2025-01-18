function randomPriceChange(stockSymbol) {
    let currentPrice = stockPrices[stockSymbol];
    currentPrice = parseFloat(currentPrice);
    //const change = (Math.random() * 2 - 1) * 0.05; // 隨機變動 -5% 到 +5%
    const change = currentPrice*(1+0.05);
    let newPrice = Math.max(0, (currentPrice * (1 + change)).toFixed(2)); // 確保價格不低於 0
    // let newPrice;
    // Record Time&date
    const nowDate = new Date(new Date().toLocaleString('zh-HK', { timeZone: 'Asia/Taipei' }));
    //times&date list of stock
    const specifiedTimesList = [
         '2025/01/18 09:00:00',
         '2025/01/18 13:30:00',
         '2025/01/18 17:00:00',
         '2025/01/18 21:00:00',
         '2025/01/19 01:00:00'
    ];
    const bankTimesList = [
        '2025/01/18 08:00:00',
        '2025/01/18 12:30:00',
        '2025/01/18 16:00:00',
        '2025/01/18 20:00:00'
    ];
    const tradingTimes = {
        "BEn-stock": specifiedTimesList,
        "WBank內銀股": bankTimesList,
        "泓國鐵路局": specifiedTimesList,
        "WTech": specifiedTimesList,
        "WTC/HKD": specifiedTimesList
    };

    const times = tradingTimes[stockSymbol];

    if (times) {
       if (stockSymbol == "BEn-stock") {
       if (nowDate >= new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00')) {
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+0.01).toFixed(2);
        } else if (nowDate >= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')){
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+10).toFixed(2);
        } else if (nowDate < new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') || nowDate > Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')) {
          newPrice = 0.01;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'none';
          });
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "已經閉市, 目前時間為 : " + nowDate;
        } else {
            newPrice = currentPrice;
        }
    } else if (stockSymbol == "WBank內銀股") {
        if (nowDate >= new Date(bankTimesList[0].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(bankTimesList[1].replace(/ /, 'T') + '+08:00')) {
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+0.01).toFixed(2);
        } else if (nowDate >= new Date(bankTimesList[1].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(bankTimesList[2].replace(/ /, 'T') + '+08:00')){
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice-20).toFixed(2);
        } else if (nowDate < new Date(bankTimesList[0].replace(/ /, 'T') + '+08:00') || nowDate > Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')) {
          newPrice = 0.956;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'none';
          });
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "已經閉市, 目前時間為 : " + nowDate;
        } else {
            newPrice = currentPrice;
        }
    } else if (stockSymbol == "泓國鐵路局") {
        if (nowDate >= new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00')) {
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+1).toFixed(2);
        } else if (nowDate >= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')){
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+6).toFixed(2);
        } else if (nowDate < new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') || nowDate > Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')) {
          newPrice = 0;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'none';
          });
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "已經閉市, 目前時間為 : " + nowDate;
        } else {
            newPrice = currentPrice;
        }
    } else if (stockSymbol == "WTech") {
        if (nowDate >= new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00')) {
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice-0.9).toFixed(2);
        } else if (nowDate >= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')){
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+0.08).toFixed(2);
        } else if (nowDate < new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') || nowDate > Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')) {
          newPrice = 0;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'none';
          });
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "已經閉市, 目前時間為 : " + nowDate;
        } else {
            newPrice = currentPrice;
        }
    } else if (stockSymbol == "WTC/HKD") {
        if (nowDate >= new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00')) {
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+0.09).toFixed(2);
        } else if (nowDate >= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')){
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice-0.2).toFixed(2);
        } else {
            newPrice = currentPrice;
        }
    }
    } else {
        newPrice = currentPrice.toFixed(2);
    }

    stockPrices[stockSymbol] = newPrice;

