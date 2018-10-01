import * as $ from 'jquery';

const main = () : void =>
{
    $(".select-classe")
        .next().find('.select-ordre').removeClass("d-none")
        .next().find('.select-famille').removeClass("d-none");
};

$(document).ready(main);