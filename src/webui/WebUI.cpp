#include "webui/WebUI.h"
#include "webui/webui_html.h"
#include "base/net/http/HttpData.h"
#include "base/net/http/HttpResponse.h"


namespace xmrig {


void WebUI::serve(const HttpData &data)
{
    HttpResponse response(data.id());
    response.setHeader(HttpData::kContentType, "text/html; charset=utf-8");
    response.setHeader("Content-Encoding", "gzip");
    response.setHeader("Cache-Control", "no-cache");

    response.end(reinterpret_cast<const char *>(kWebUiHtml), kWebUiHtmlSize);
}


} // namespace xmrig
