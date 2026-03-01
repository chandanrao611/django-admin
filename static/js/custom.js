$(document).on('click', '.navbar-toggler', function (ent) {
	// if ($('body').hasClass('sidebar-lg-show')) {
	// 	$('body').removeClass('sidebar-lg-show')
	// }
	// else {
	// 	$('body').addClass('sidebar-lg-show')
	// }
	if ($('#sidebar').hasClass('active')) {
		$('#sidebar').removeClass('active')
	}
	else {
		$('#sidebar').addClass('active')
	}
})
$(document).on('click', '#navbar-toggler-rao', function (ent) {
	if ($('body').hasClass('sidebar-icon-only')) {
		$('body').removeClass('sidebar-icon-only')
	}
	else {
		$('body').addClass('sidebar-icon-only')
	}
})
$(document).ready(function () {
	$('input').on('drop', function () {
		return false;
	});
});
$(document).on('keypress keyup blur', '.search-input-box', function (event) {
	var classStr = $(this).attr('class'),
		lastClass = classStr.substr(classStr.lastIndexOf(' ') + 1);
	debounceTime($(this).val());
	// $('#' + lastClass).trigger('change');
	// $('select#' + lastClass).each(function (index, obj) {
	// });
});

let counter = 0;
const getData = (restArg) => {
}
const magicSearch = function (fn, d) {
	let timer;
	return function () {
		let context = this;
		clearTimeout(timer);
		timer = setTimeout(() => {
			fn.apply(context, arguments)
		}, d);
	}
}
const debounceTime = magicSearch(getData, 500);

$('.checked_all').on('change', function () {
	$('.checkbox').prop('checked', $(this).prop("checked"));
});
// deselect "checked all", if one of the listed checkbox product is unchecked amd select "checked all" if all of the listed checkbox product is checked
$('.checkbox').change(function () { //".checkbox" change 
	if ($('.checkbox:checked').length == $('.checkbox').length) {
		$('.checked_all').prop('checked', true);
	} else {
		$('.checked_all').prop('checked', false);
	}
});
/*
* Select all text of input field
*/
$(document).bind('cut copy paste', '.not_ccp', function (e) {
	//e.preventDefault();
});
/*
* Select all text of input field
*/
$(document).on('click', '.select_all', function () {
	$(this).select();
});
/*
* Allow only numeric value in input field ex: 20, 30
*/
$(document).on('keypress keyup blur', '.number', function (event) {
	$(this).val($(this).val().replace(/[^\d].+/, ""));
	if ((event.which < 48 || event.which > 57)) {
		event.preventDefault();
	}
});
/*
* Allow only decimal value in input field ex: 20.59, 30.00
* This function not alow more than one decimal point 
*/
$(document).on('keypress keyup blur', '.decimal', function (event) {
	$(this).val($(this).val().replace(/[^0-9\.]/g, ''));
	if ((event.which != 46 || $(this).val().indexOf('.') != -1) && (event.which < 48 || event.which > 57)) {
		event.preventDefault();
	}
});
/*
* not allow white spaces
*/
$(document).on('keypress keyup blur', '.notwhitespace', function (event) {
	var k = event ? event.which : window.event.keyCode;
	if (k == 32) return false;
});
/*
*   Not allow special character into the input field
*/
$(document).on('keypress keyup blur', '.not_special_char', function (e) {
	var k = e.keyCode,
		$return = ((k > 64 && k < 91) || (k > 96 && k < 123) || k == 8 || k == 32 || (k >= 48 && k <= 57));
	if (!$return) {
		return false;
	}
});
/*
* To verify valid email formate
*/
$(document).on('blur', '.valid_email', function (e) {
	var patern = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
	if (!patern.test(this.value)) {
		$(this).next("span").remove();
		$(this).after("<span style='color:red;font-size: 14px;font-style: italic;font-weight: 500;'>Please enter valid email address.</span>");
	}
});
/*
*   To remove error message
*/
$(document).on('keypress', '.valid_email', function (e) {
	$(this).next("span").remove();
});
/*
*   To validate input multiple email address seperated by , (comma)
*/
$(document).on('blur', '.multi_valid_email', function (e) {
	var emails = $(this).val().trim();
	var result = emails.replace(/\s/g, "").split(/,|;/);
	var errors = [];
	for (var i = 0; i < result.length; i++) {
		if (!validateEmail(result[i])) {
			errors[i] = result[i] + ' is not valid email address.';
		}
	} /// end of the for loop
	if (errors.length > 0) {
		$(this).next("span").remove();
		$(this).after("<span style='color:red;font-size: 14px;font-style: italic;font-weight: 500;'>" + errors.join('\n') + "</span>");
		return false;
	}
	else {
		$(this).next("span").remove();
		return true;
	}//// end of else block
});

function validateEmail(value) {
	var regex = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
	return (regex.test(value)) ? true : false;
}

window.addEventListener('storage', (event) => {
	if (event.storageArea == localStorage) {
		let token = localStorage.getItem('User_Detail_Token');
		if (token == undefined) {
			window.location.href = `${window.location.origin}/#/`
		}
	}
}, false);
$(function () {
	$('#sidebar a').filter(function () {
		return this.href == location.href
	}).parent().addClass('active').siblings().removeClass('active')

	$('#sidebar a').click(function () {
		$(this).parent().addClass('active').siblings().removeClass('active')
	})
	$('.parent').click(function (b) {
		$('.collapse').removeClass('show');
		$('.toggle').attr('aria-expanded', false);
	});
	$('#sidebar a.toggle').click(function (e) {
		if ($(this).siblings().hasClass('show')) {
			// $(this).siblings().removeClass('show');
		}
		else {
			$('.nav-item').not(this).each(function (a, b) {
				$(b).find('div.collapse.show').each(function (x, y) {
					$(this).removeClass('show');
				});
			});
		}
	});
});
$(document).ready(function () {
	$('[data-toggle="tooltip"]').tooltip();
});

document.addEventListener("DOMContentLoaded", function() {
    function OTPInput() {
        const inputs = document.querySelectorAll('#otp > input');
        for (let i = 0; i < inputs.length; i++) {
            inputs[i].addEventListener('input', function() {
                if (this.value.length > 1) {
                    this.value = this.value[0]; //
                }
                if (this.value !== '' && i < inputs.length - 1) {
                    inputs[i + 1].focus(); //
                }
            });

            inputs[i].addEventListener('keydown', function(event) {
                if (event.key === 'Backspace') {
                    this.value = '';
                    if (i > 0) {
                        inputs[i - 1].focus();
                    }
                }
            });
        }
    }

    OTPInput();
});