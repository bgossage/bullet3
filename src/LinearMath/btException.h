/*
Copyright (c) 2014 Brett Gossage  http://github.com/bgossage

This software is provided 'as-is', without any express or implied warranty.
In no event will the authors be held liable for any damages arising from the use of this software.
Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it freely,
subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software.
   If you use this software in a product, an acknowledgment in the product documentation would be appreciated
   but is not required.
2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.
*/

#include <exception>
#include <string>


#ifndef BT_EXCEPTION_H
#define BT_EXCEPTION_H

/**
* Common base class for exception handling.
* in the Bullet3 library
*/
class btException : public std::exception
{
   public:
   /// Constructor
      explicit btException( std::string reason,
                            std::string scope,
                            std::string file,
                            int line = 0
                          );

   /// Destructor
      virtual ~btException() throw();

   /// Returns the exception reason.
      virtual const char* what() const throw();

   protected:
      std::string m_reason;

}; // end class btException


#ifdef __GNUC__
#define BT_EXCEPTION_SCOPE __PRETTY_FUNCTION__
#endif

#if _WIN32
#if _MSC_VER >= 1300
#define BT_EXCEPTION_SCOPE __FUNCSIG__
#endif
#endif

#if !defined( BT_EXCEPTION_SCOPE )
#define BT_EXCEPTION_SCOPE "unknown"
#endif

#define BT_XMSG_STR( STR ) BT_MSG_STR( STR )
#define BT_MSG_STR( STR ) #STR

/**
* A macro for throwing exceptions of type btException.
* The file, line number, and scope at the point of the throw
* are passed to the exception constructor.
*/
#ifndef __SPU__
#define BT_THROW_MESSAGE( msg ) \
             throw btException( ( msg ), BT_EXCEPTION_SCOPE, __FILE__, __LINE__ )
#else
#define BT_THROW_MESSAGE( msg ) ((void)0)
#endif


#endif

// EOF

