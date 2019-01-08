function switchTab(evt, attendance) {
    if(attendance === 'all'){
        $('#all').css('display','block');
        $('#present').css('display','none');
        $('#present_extras').css('display','block');
    }

    if(attendance === 'present'){
        $('#all').css('display','none');
        $('#present').css('display','block');
        $('.absentPeople').css('display','none');
        $('.extra_people').css('display: none');

        if($('.presentPeople').length != 0){
            $('#emptylist').css('display','none');
            $('.presentPeople').css('display','table-row');
        }else{
            $('#present').css('display','none');
            $('#emptylist').css('display','block');
        }  
    }

    if(attendance === 'absent'){
        $('#all').css('display','none');
        $('#present').css('display','block');
        $('.presentPeople').css('display','none');
        $('.extra_people').css('display: none');

        if($('.absentPeople').length != 0){
            $('#emptylist').css('display','none');
            $('.absentPeople').css('display','table-row');
        }else{
            $('#present').css('display','none');
            $('#emptylist').css('display','block');
        }  
    }

    if(attendance === 'present_extras'){
        $('#all').css('display','none');
        $('#present').css('display','block');
        $('.presentPeople').css('display','none');
        $('.absentPeople').css('display','none');

        if($('.extra_people').length != 0){
            $('#emptylist').css('display','none');
            $('.extra_people').css('display','table-row');
        }else{
            $('#present').css('display','none');
            $('#emptylist').css('display','block');
        }  

    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    evt.currentTarget.className += " active";

}