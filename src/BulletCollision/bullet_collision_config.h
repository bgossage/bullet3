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


#ifndef BULLET_COLLISION_CONFIG
#define BULLET_COLLISION_CONFIG

// DLL specifiers...
#ifdef WIN32
   #ifdef BulletCollision_EXPORTS
      #define BULLET_COLLISION_EXPORT __declspec( dllexport )
   #else
      #define BULLET_COLLISION_EXPORT __declspec( dllimport )
   #endif
#else
   #define BULLET_COLLISION_EXPORT
#endif



#endif

// EOF
