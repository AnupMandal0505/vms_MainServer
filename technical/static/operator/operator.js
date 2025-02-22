function setuserLimitFormModelData(userId, current_new_limit) {
    document.getElementById("user_limit_id").value = userId;
    document.getElementById("CurrentUserLimit").innerHTML = current_new_limit;

    document.getElementById("new_limit").addEventListener("input", function (e) {
        this.value = this.value.replace(/[^0-9]/g, ''); // Allow only numbers
        // if (this.value.length > 10) {
        //     this.value = this.value.slice(0, 10); // Limit input to 10 digits
        // }
    });
}



function setClientUSerModalData(userId, is_on_hold,delete_account) {
    document.getElementById("manage_account_id").value = userId;
    if (is_on_hold === "true") {
        document.getElementById("deactivate").checked = true;
        document.getElementById("activate").checked = false;
    } else {
        document.getElementById("activate").checked = true;
        document.getElementById("deactivate").checked = false;
    }

    if (delete_account === "true") {
        document.getElementById("delete").checked = true;
    } else {
        document.getElementById("delete").checked = false;
    }
}





function setClientRequestModalData(userId) {
    document.getElementById("user_request_id").value = userId;
}