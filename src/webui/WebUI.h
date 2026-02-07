#ifndef XMRIG_WEBUI_H
#define XMRIG_WEBUI_H


#include <cstdint>


namespace xmrig {


class HttpData;


class WebUI
{
public:
    static void serve(const HttpData &data);
};


} // namespace xmrig


#endif // XMRIG_WEBUI_H
