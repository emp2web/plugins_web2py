#from plugin_filterLocals import FilterLocals

def filter():
	filter_js = URL('static', 'plugin_filterLocals/js/fcjs.min.js')

	a=XML(
        	"""
        	<script type="text/javascript" src="%(filter_js)s"></script>
        	""" % dict(filter_js=filter_js)
        	)
	b=XML(
			"""
				<script type="text/javascript">
					jQuery(function() {
						$('table').fcJS({
							inputStyle: 'width: 50px; display: block;'
						});
					});
				</script>
			"""
			)
	return a,b