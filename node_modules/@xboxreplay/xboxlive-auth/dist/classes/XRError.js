"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var XRErrorReasons;
(function (XRErrorReasons) {
    XRErrorReasons["BAD_REQUEST"] = "BAD_REQUEST";
    XRErrorReasons["UNAUTHORIZED"] = "UNAUTHORIZED";
    XRErrorReasons["FORBIDDEN"] = "FORBIDDEN";
    XRErrorReasons["NOT_FOUND"] = "NOT_FOUND";
    XRErrorReasons["TOO_MANY_REQUESTS"] = "TOO_MANY_REQUESTS";
    XRErrorReasons["INTERNAL_ERROR"] = "INTERNAL_ERROR";
})(XRErrorReasons || (XRErrorReasons = {}));
const statusCodeToReasonMap = {
    500: 'INTERNAL_ERROR',
    400: 'BAD_REQUEST',
    401: 'UNAUTHORIZED',
    403: 'FORBIDDEN',
    404: 'NOT_FOUND',
    429: 'TOO_MANY_REQUESTS'
};
const defaultErrorMessage = 'Something went wrong...';
const defaultStatusCode = 500;
const defaultReason = XRErrorReasons.INTERNAL_ERROR;
class XRError extends Error {
    constructor(message = defaultErrorMessage, details = {}) {
        super(message);
        this.__XboxReplay__ = true;
        this.details = {
            statusCode: defaultStatusCode,
            reason: defaultReason,
            additional: null
        };
        this.name = this.constructor.name;
        if (typeof Error.captureStackTrace === 'function')
            Error.captureStackTrace(this, this.constructor);
        else
            this.stack = new Error(message).stack;
        this.details = Object.assign(Object.assign({}, this.details), details);
        this.details.reason =
            statusCodeToReasonMap[this.details.statusCode] ||
                statusCodeToReasonMap[defaultStatusCode];
    }
    getMessage() {
        return this.message;
    }
    getDetails() {
        return this.details;
    }
    getStatusCode() {
        return this.getDetails().statusCode;
    }
    getReason() {
        return this.getDetails().reason;
    }
    getAdditional() {
        return this.getDetails().additional;
    }
}
XRError.badRequest = (message = 'Bad Request', additional = null) => new XRError(message, {
    statusCode: 400,
    additional
});
XRError.unauthorized = (message = 'Unauthorized', additional = null) => new XRError(message, {
    statusCode: 401,
    additional
});
XRError.forbidden = (message = 'Forbidden', additional = null) => new XRError(message, {
    statusCode: 403,
    additional
});
XRError.tooManyRequests = (message = 'Too Many Requests', additional = null) => new XRError(message, {
    statusCode: 429,
    additional
});
XRError.internal = (message = 'Internal Error', additional = null) => new XRError(message, {
    statusCode: 500,
    additional
});
exports.default = XRError;
