if (stockSymbol == "BEn-stock") {
       if (nowDate >= new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00')) {
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+100).toFixed(2);
        } else if (nowDate >= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')){
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+10).toFixed(2);
        } else if (nowDate < new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') || nowDate > Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')) {
          newPrice = 0;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'none';
          });
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "已經閉市, 目前時間為 : " + nowDate;
        }
    } else if (stockSymbol == "WBank內銀股") {
        if (nowDate >= new Date(bankTimesList[0].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(bankTimesList[1].replace(/ /, 'T') + '+08:00')) {
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+100).toFixed(2);
        } else if (nowDate >= new Date(bankTimesList[1].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(bankTimesList[2].replace(/ /, 'T') + '+08:00')){
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice-20).toFixed(2);
        } else if (nowDate < new Date(bankTimesList[0].replace(/ /, 'T') + '+08:00') || nowDate > Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')) {
          newPrice = 0;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'none';
          });
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "已經閉市, 目前時間為 : " + nowDate;
        }
    } else if (stockSymbol == "泓國鐵路局") {
        if (nowDate >= new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00')) {
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+100).toFixed(2);
        } else if (nowDate >= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')){
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+10).toFixed(2);
        } else if (nowDate < new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') || nowDate > Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')) {
          newPrice = 0;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'none';
          });
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "已經閉市, 目前時間為 : " + nowDate;
        }
    } else if (stockSymbol == "WTech") {
        if (nowDate >= new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00')) {
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice-10).toFixed(2);
        } else if (nowDate >= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')){
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+30).toFixed(2);
        } else if (nowDate < new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') || nowDate > Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')) {
          newPrice = 0;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'none';
          });
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "已經閉市, 目前時間為 : " + nowDate;
        }
    } else if (stockSymbol == "WTC/HKD") {
        if (nowDate >= new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00')) {
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice-95).toFixed(2);
        } else if (nowDate >= new Date(specifiedTimesList[1].replace(/ /, 'T') + '+08:00') && nowDate <= new Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')){
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "目前時間為 : " + nowDate;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'block';
          });
          newPrice = (currentPrice+20).toFixed(2);
        } else if (nowDate < new Date(specifiedTimesList[0].replace(/ /, 'T') + '+08:00') || nowDate > Date(specifiedTimesList[2].replace(/ /, 'T') + '+08:00')) {
          newPrice = 0;
          document.querySelectorAll('#availableStocks tr').forEach(row => {
            row.style.display = 'none';
          });
          document.getElementById('tradeHintText').style.display = 'block';
          document.getElementById('tradeHintText').innerHTML = "已經閉市, 目前時間為 : " + nowDate;
        }
    } else {
        newPrice = currentPrice.toFixed(2);
    }

    stockPrices[stockSymbol] = newPrice;
