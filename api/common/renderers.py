from rest_framework.renderers import JSONRenderer

class SiteJsonRenderer(JSONRenderer):
	def render(self, data, media_type=None, renderer_context=None):
		"""
		Renders HTTP responses for the WeddingSite API applications.
		Each response contains a 'data' and 'error' key with list
		payloads.  
		"""
		response = renderer_context.get("response")
		new_response = {
			'data': [],
			'errors': []
		}

		if response.status_code < 400:
			new_response['data'] = data
		else:
			error_list = []

			for key in data:
				error_list.append(
					{
						"status": response.status_code,
						"error_key": key,
						"detail": data[key][0]
					}
				)
			new_response['errors'].append(error_list)

		return super(SiteJsonRenderer, self).render(
			data=new_response, renderer_context=renderer_context)
			