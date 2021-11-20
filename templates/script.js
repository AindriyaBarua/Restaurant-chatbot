function getBotResponse() {
          var rawText = $("#nameInput").val();
          var userHtml = '<p class="userText"><span><b>' + "You : " + '</b>' + rawText + "</span></p>";
          $("#nameInput").val("");
          $("#chatbox").append(userHtml);
          document
            .getElementById("userInput")
            .scrollIntoView({ block: "start", behavior: "smooth" });
          $.get("/get", { msg: rawText }).done(function(data) {
            var botHtml = '<p class="botText"><span><b>' + "Restrobot : " + '</b>' + data + "</span></p>";
            $("#chatbox").append(botHtml);
            document
              .getElementById("userInput")
              .scrollIntoView({ block: "start", behavior: "smooth" });
          });
        }
        $("#nameInput").keypress(function(e) {
          if (e.which == 13) {
            getBotResponse();
          }
        });