declare type XRErrorDetails = {
    statusCode: number;
    reason: keyof typeof XRErrorReasons;
    additional: any;
};
declare enum XRErrorReasons {
    BAD_REQUEST = "BAD_REQUEST",
    UNAUTHORIZED = "UNAUTHORIZED",
    FORBIDDEN = "FORBIDDEN",
    NOT_FOUND = "NOT_FOUND",
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS",
    INTERNAL_ERROR = "INTERNAL_ERROR"
}
declare class XRError extends Error {
    readonly __XboxReplay__ = true;
    readonly details: XRErrorDetails;
    static badRequest: (message?: string, additional?: XRErrorDetails['additional']) => XRError;
    static unauthorized: (message?: string, additional?: XRErrorDetails['additional']) => XRError;
    static forbidden: (message?: string, additional?: XRErrorDetails['additional']) => XRError;
    static tooManyRequests: (message?: string, additional?: XRErrorDetails['additional']) => XRError;
    static internal: (message?: string, additional?: XRErrorDetails['additional']) => XRError;
    constructor(message?: string, details?: Omit<Partial<XRErrorDetails>, 'reason'>);
    getMessage(): string;
    getDetails(): XRErrorDetails;
    getStatusCode(): number;
    getReason(): keyof typeof XRErrorReasons;
    getAdditional(): Record<string, string> | null;
}
export default XRError;
