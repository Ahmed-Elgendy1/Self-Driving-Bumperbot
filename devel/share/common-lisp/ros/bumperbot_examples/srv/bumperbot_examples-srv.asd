
(cl:in-package :asdf)

(defsystem "bumperbot_examples-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "AddTwoints" :depends-on ("_package_AddTwoints"))
    (:file "_package_AddTwoints" :depends-on ("_package"))
    (:file "GetTransform" :depends-on ("_package_GetTransform"))
    (:file "_package_GetTransform" :depends-on ("_package"))
  ))