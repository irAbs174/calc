$(function () {
    //fancyfileuplod


    $('#demo').FancyFileUpload({
        params: {
            action: 'fileuploader'
        },
        maxfilesize: 1000000
    });

});