

function renderWithNotesType(event, element, view) {
	//alert(view.name);
	var colorclass='';
	if(event.note_type == '1'){
		colorclass = 'memo_color';
	}else if(event.note_type == '2'){
		colorclass = 'invest_color';
	}else if(event.note_type == '3'){
		colorclass = 'account_color';
	}
	
	event['colorClassName'] = colorclass;
	
	
	element.addClass(colorclass)
				.find('.fc-title')
					.html(renderNotesHtml(event,view));
}

function renderNotesHtml(event,view){
	var _iclass = '', _html = '', _rmk = '';
	if(event.note_type == '1'){
		_iclass = ' fa-calendar';
	}else if(event.note_type == '2'){
		_iclass = ' fa-money';
	}else if(event.note_type == '3'){
		_iclass = ' fa-book';
	}

	event['typeClassName'] = _iclass;
	
	if(view.name == 'month'){
		_html= ['<i class="fa ', _iclass ,'"><span class="smpad">',event.note_type_name,
		        '</span></i>'].join("");
	}else if(view.name=='agendaWeek'){
		_html= ['<i class="fa ', _iclass ,'"><span class="smpad">',event.title,
		        '</span></i>'].join("");
	}else if(view.name=='agendaDay'){
		_rmk =  (event.remark && event.remark.length >= 30) ? 
					event.remark.substring(0,30)+"..." : event.remark;
		_html= ['<i class="fa ', _iclass ,'"><span class="smpad">',
		        event.note_type_name,'-',event.title,'</span><br><div class="remark_line">',
		        _rmk,'</div></i>' ].join("");
	}

	return _html;
}

function getParamJson(){
	var arr = [];
	$(".notes").filter(function() {
		return $(this).hasClass(this.id + "_color");
	}).each(function() {
		if (this.id == 'memo') {
			arr.push(1);
		} else if (this.id == 'invest') {
			arr.push(2);
		} else if (this.id == 'account') {
			arr.push(3);
		}
	});
	return {"note_type": arr}
}


