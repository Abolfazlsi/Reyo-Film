function rating(slug) {
    var rate = document.getElementById("rating")
    var rate_count = document.getElementById("rate_count")

    $.get(`/serial/serial-rating/${slug}`).then(response => {
        if (response["response"] === "rating") {
            rate.className = "fa fa-heart"
            rate_count.innerText = Number(rate_count.innerText) + 1
        } else {
            rate.className = "fa fa-heart-o"
            rate_count.innerText = Number(rate_count.innerText) - 1

        }
    })
}
