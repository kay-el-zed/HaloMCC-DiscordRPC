"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.getBaseHeaders = void 0;
const config_1 = __importDefault(require("../config"));
const getBaseHeaders = (additionalHeaders = {}) => (Object.assign({ Pragma: 'no-cache', Accept: '*/*', 'User-Agent': config_1.default.request.defaultUserAgent, 'Cache-Control': 'no-store, must-revalidate, no-cache', 'Accept-Encoding': 'gzip, deflate, compress', 'Accept-Language': `${config_1.default.request.defaultLanguage}, ${config_1.default.request.defaultLanguage.split('-')[0]};q=0.9` }, additionalHeaders));
exports.getBaseHeaders = getBaseHeaders;
