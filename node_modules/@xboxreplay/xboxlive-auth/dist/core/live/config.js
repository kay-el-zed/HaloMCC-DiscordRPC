"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.defaultResponseType = exports.defaultRedirectUri = exports.defaultScope = exports.defaultClientId = void 0;
exports.defaultClientId = '000000004C12AE6F';
exports.defaultScope = 'service::user.auth.xboxlive.com::MBI_SSL';
exports.defaultRedirectUri = 'https://login.live.com/oauth20_desktop.srf';
exports.defaultResponseType = 'token';
exports.default = {
    urls: {
        authorize: 'https://login.live.com/oauth20_authorize.srf',
        token: 'https://login.live.com/oauth20_token.srf'
    },
    client: {
        id: exports.defaultClientId,
        redirectUri: exports.defaultRedirectUri,
        scope: exports.defaultScope,
        responseType: exports.defaultResponseType
    }
};
