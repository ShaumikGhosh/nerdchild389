$(document).ready(function () {

    let x = function rollDice() {
        return (Math.floor(Math.random() * 60000) + 70000);
    };

    let collectedData = [];

    $("#form-one").css('display', 'block');
    $('.petBar1').addClass('petBar1Complete');
    $('.petRact1').addClass('petRact1Complete');

    $(document).on('submit', '#form-one', function (e) {

        e.preventDefault();

        let petName = $('#pet-name').val();

        if (petName !== "") {

            collectedData.push(petName);

            $("#form-one").css('display', 'none');
            $("#info-from").css('display', 'block');
            $('.petBar2').addClass('petBar2Complete');
            $('.petRact2').addClass('petRact2Complete');
            return false;
        } else {
            let message = "Pet name is required!";
            displayError(message);
            return false;
        }
    });

    $(document).on('submit', '#info-from', function (e) {

        e.preventDefault();

        let petBreed = $('#pet-breed').val();
        let petAge = $('#pet-age').val();
        let petWeight = $('#pet-weight').val();

        if (petBreed !== "" && petAge !== "" && petWeight !== "") {

            collectedData.push(petBreed);
            collectedData.push(petAge);
            collectedData.push(petWeight);
            collectedData.push(x());

            $.ajax({
                type: "POST",
                url: "",
                data: {
                    'pet-name': collectedData[0],
                    'pet-breed': collectedData[1],
                    'pet-age': parseInt(collectedData[2]),
                    'pet-weight': parseInt(collectedData[3]),
                    'uni-pk': collectedData[4],
                },
            });

            $("#form-one").css('display', 'none');
            $("#info-from").css('display', 'none');
            $("#problem-form").css('display', 'block');
            $('.petBar3').addClass('petBar3Complete');
            $('.petRact3').addClass('petRact3Complete');

            sessionStorage.setItem('pet_key', collectedData[4]);

            let data = [
                collectedData[0],
                collectedData[1],
                collectedData[2],
                collectedData[3],
            ];
            localStorage.setItem('data', data);

            return false;
        } else {
            let message = "All fields are required!";
            displayError(message);
            return false;
        }

    });

    $(document).on('submit', '#problem-form', function (e) {

        e.preventDefault();

        if ($('input[name="problem"]:checked').val()) {

            $.ajax({
                type: "POST",
                url: "/symptom/",
                data: {
                    'problem': $('input[name="problem"]:checked').val(),
                    'hidden-uni-pk': sessionStorage.getItem('pet_key'),
                },
            });

            $("#form-one").css('display', 'none');
            $("#info-from").css('display', 'none');
            $("#problem-form").css('display', 'none');
            $(".result").css('display', 'block');
            $('.petBar4').addClass('petBar4Complete');
            $('.petRact4').addClass('petRact4Complete');

            localStorage.setItem('data2', $('input[name="problem"]:checked').val());

            setTimeout(function () {
                displayResult();
            },);
            return false;
        } else {
            let message = "Issue selection is required!";
            displayError(message);
            return false;
        }

    });

    $(document).on('submit', '#mail-form', function (e) {

        e.preventDefault();

        let email = $('#email').val();
        let username = $('#username').val();
        let message = $('#message').val();
        let regx = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

        $("#form-one").css('display', 'none');
        $("#info-from").css('display', 'none');
        $("#problem-form").css('display', 'none');
        $(".result").css('display', 'none');
        $(".tank-you-area").css('display', 'block');
        $('.petBar5').addClass('petBar5Complete');
        $('.petRact5').addClass('petRact5Complete');
        $('.petBar6').addClass('petBar6Complete');

        successMessage(username);

        return false;
    });
    $('#rsbtn2').click(function () {

        $("#form-one").css('display', 'none');
        $("#info-from").css('display', 'none');
        $("#problem-form").css('display', 'none');
        $(".result").css('display', 'none');
        $(".tank-you-area").css('display', 'block');
        $('.petBar5').addClass('petBar5Complete');
        $('.petRact5').addClass('petRact5Complete');
        $('.petBar6').addClass('petBar6Complete');
        return false;
    });

    $('#back-home').click(function () {
        window.location.href = "";
        return false;
    });
});

function displayError(msg) {
    $('.swt-popup').append(`
        <script>
            Swal.fire({
                icon: 'error',
                text: '${msg}',
            });
        </script>
    `);
}

function successMessage(name) {
    $('.swt-popup').append(`
        <script>
            Swal.fire(
                'Great!',
                "Hello ${name}, Thanks for mailing us, we'll contact you shortly!",
                'success',
            )
        </script>
    `);
}

function displayResult() {

    let c = localStorage.getItem('data');
    let b = c.split(",");

    $('#pet_name').append(`${b[0]}.`);
    $('#pet_breed').append(`${b[1]}.`);
    $('#pet_age').append(`${b[2]} years old.`);
    $('#pet_weight').append(`${b[3]} kg.`);

    let pb = localStorage.getItem('data2');

    if (pb === "ca"){
        $('#pet_problem').append("Chronic Anxiety.");
        localStorage.setItem('problem', "Chronic Anxiety")
    }
    if (pb === "is"){
        $('#pet_problem').append("Itching/Scratching.");
        localStorage.setItem('problem', "Itching/Scratching")
    }
    if (pb === "pn"){
        $('#pet_problem').append("Pain.");
        localStorage.setItem('problem', "Pain")
    }

    if(localStorage.getItem('problem') ==="Chronic Anxiety"){
        $('#solution').append("Stress Reliever.");
        $('#product-img').attr("src", "static/frontend/images/cbd-oil.jpg");
    }
    if(localStorage.getItem('problem') ==="Itching/Scratching"){
        $('#solution').append("Veterinarian Consult.");
        $('#product-img').attr("src", "static/frontend/images/cbd-oil.jpg");
    }
    if(localStorage.getItem('problem') ==="Pain"){
        $('#solution').append("Stress Reliever, Veterinarian Consult");
        $('#product-img').attr("src", "static/frontend/images/cbd-oil.jpg");
    }
}
