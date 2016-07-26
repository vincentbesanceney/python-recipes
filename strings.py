class MagicString(str):

    '''A string subclass with magic power.

    A magic string evaluates to its formatted string, as specified by the spell
    static method. The original string is stored in the 'origin' attribute. This
    is useful when we want to transform a string while retaining the original
    value.

    Example #1: Hashed string -- A Hash object provides the digest of the string
    used during instantiation, while retaining the original string value in the
    origin attribute.

        >>> from hashlib import sha1
        >>> class Hash(MagicString):
        ...     @staticmethod
        ...     def spell(s):
        ...         return sha1(s).hexdigest()
        >>> h = Hash('mystring')
        >>> h
        9ce3ea4d6fac2165933b3971e6d5a13753c7d878
        >>> h.origin
        mystring

    Example #2: Hidden password -- If by mistake we print out the password asked
    to a user, e.g. as we log some parameters of a command-line for debugging
    purpose, the transformed version of the string will be printed, instead of
    the original version. To use the original string, we must be explicit.

        >>> class Password(MagicString):
        ...     @staticmethod
        ...     def spell(s):
        ...         return '*****'
        >>> pw = Password('secret')
        >>> pw
        *****
        >>> pw.origin
        secret

    '''

    @staticmethod
    def spell(string):
        return string

    def __new__(cls, string, *args, **kwargs):
        instance = str.__new__(cls, cls.spell(string))
        instance.origin = string
        return instance
