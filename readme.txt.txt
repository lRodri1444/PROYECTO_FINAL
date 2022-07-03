PROYECTO FINAL - BLOG
----------------------
Autor (Único miembro): Luis Felipe Rodriguez Carrasco

Rutas : Todas las rutas tienen botones configurados.
----------------------

• HOME : <puerto>/home

Accede al home del blog, desde el que se puede crear posts y ver los posts de los demás usuarios.


• PROFILE : <puerto>/home/profile

Accede al perfil del usuario logueado, desde el que se puede visualizar, editar y eliminar posts propios.


• PROFILES : <puerto>/home/profiles/<profile_id>

Accede al perfil de otros usuarios y visualiza sus posts.
Nota : Acceder a la ruta con el id del usuario logueado redirigirá automaticamente a <puerto>/home/profile

• PAGES : <puerto>/home/pages

Pestaña desde que se puede leer, editar o eliminar cualquier post de la página.
Nota : Solo un superuser puede entrar a esta ruta. Un boton aparecerá para el superusuario en la navbar

• PAGES ID : <puerto>/home/pages/<post_id>

Accede al detalle de un post.
Cualquier usuario puede entrar


• AUTHENTICATION EDIT : <puerto>/home/edit

Permite al usuario logueado editar sus datos de autenticación : Usuario, correo, contraseña.


• PROFILE EDIT : <puerto>/home/extra_edit

Permite al usuario logueado editar su biografia y su foto de perfil que es usado como avatar.


• UPDATE POST : <puerto>/home/update_page/<post_id>

Permite editar el titulo y el cuerpo de un post en el editor ckeditor.
Nota : Solo el dueño del post o un superuser pueden realizar la acción. Aun si se intenta desde
otra cuenta ingresando la ruta desde el buscador, redirigirá a <puerto>/home


• DELETE POST : <puerto>/home/delete_page/<post_id>
Nota : Solo el dueño del post o un superuser pueden realizar la acción. Aun si se intenta desde
otra cuenta ingresando la ruta desde el buscador, redirigirá a <puerto>/home/profile


---------------------