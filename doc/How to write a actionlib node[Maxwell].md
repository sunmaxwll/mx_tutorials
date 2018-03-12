# 准备功能包以及action消息文件 
## 工作空间 
~/catkin_ws/

## 功能包建立位置 
cd ~/catkin_ws/src

catkin_create_pkg mx_tutorials actionlib message_generation roscpp rospy std_msgs actionlib_msgs

cd ~/catkin_ws/src/mx_tutorials/

## 建立Test.action文件 

cd ~/catkin_ws/src/mx_tutorials/

mkdir action

cd action

touch Test.action

## 添加action文件内容(根据你的需求，此处以roswiki的fibonacci为例) 
```
    #goal definition
    int32 order
    ---
    #result definition
    int32[] sequence
    ---
    #feedback
    int32[] sequence
```

## 配置CMakeLists.txt文件 

确保以下内容存在，使用catkin_create_pkg时，已经加入了actionlib_msgs的相关信息。
主要是手动添加： 
```
add_action_files(
  DIRECTORY action
  FILES
  Test.action
)
```

必须要有的条目： 
```
find_package(catkin REQUIRED COMPONENTS
  rospy
  actionlib_msgs
)

add_action_files(
  DIRECTORY action
  FILES
  Test.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs
  std_msgs  # Or other packages containing msgs
)

catkin_package(
  CATKIN_DEPENDS actionlib_msgs
)
```

## 配置package.xml 
确保以下内容存在，使用catkin_create_pkg时，已经加入了actionlib_msgs的相关信息。
```
  <build_depend>rospy</build_depend>
  <build_depend>actionlib_msgs</build_depend>
  <build_export_depend>rospy</build_export_depend>
  <exec_depend>rospy</exec_depend>
  <exec_depend>actionlib_msgs</exec_depend>
  <exec_depend>message_generation</exec_depend>
```

## 编译功能包mx_tutorials 

cd ~/catkin_ws/src

catkin_make

## catkin_make后将会在devel中生成的msg文件 
cd ~/catkin_ws/devel/share/mx_tutorials/msg

ls -lh

total 28K
-rw-rw-r-- 1 aicuijie aicuijie 141 Mar 12 02:22 TestActionFeedback.msg
-rw-rw-r-- 1 aicuijie aicuijie 130 Mar 12 02:22 TestActionGoal.msg
-rw-rw-r-- 1 aicuijie aicuijie 165 Mar 12 02:22 TestAction.msg
-rw-rw-r-- 1 aicuijie aicuijie 137 Mar 12 02:22 TestActionResult.msg
-rw-rw-r-- 1 aicuijie aicuijie  99 Mar 12 02:22 TestFeedback.msg
-rw-rw-r-- 1 aicuijie aicuijie 100 Mar 12 02:22 TestGoal.msg
-rw-rw-r-- 1 aicuijie aicuijie 107 Mar 12 02:22 TestResult.msg

## 使用rosmsg list | grep mx_tutorials查看在ROS中的msg 
rosmsg list | grep mx_tutorials 

mx_tutorials/TestAction
mx_tutorials/TestActionFeedback
mx_tutorials/TestActionGoal
mx_tutorials/TestActionResult
mx_tutorials/TestFeedback
mx_tutorials/TestGoal
mx_tutorials/TestResult

# 编写一个actionlib服务端 

* 复制一份roswiki的[Fibonacci 服务端例程](https://wiki.ros.org/actionlib_tutorials/Tutorials/SimpleActionServer(ExecuteCallbackMethod)) 
* 替换actionlib_tutorials.msg为mx_tutorials.msg 
    注意我们的功能包名为mx_tutorials，所以需要将例程中的actionlib_tutorials修改掉。 
* 替换Fibonacci为Test 
    注意理解这里的操作，其目的在于修改正确调用消息的名字：我们的功能包生成的action的消息文件名(catkin_make后将会在devel中生成的msg文件)。 

# 编写一个actionlib客户端 

* 复制一份roswiki的[Fibonacci 客户端例程](https://wiki.ros.org/actionlib_tutorials/Tutorials/Writing a Simple Action Client (Python)) 
* 替换actionlib_tutorials.msg为mx_tutorials.msg 
    注意我们的功能包名为mx_tutorials，所以需要将例程中的actionlib_tutorials修改掉。 
* 替换Fibonacci为Test 
    注意理解这里的操作，其目的在于修改正确调用消息的名字：我们的功能包生成的action的消息文件名(catkin_make后将会在devel中生成的msg文件)。 

#### 阳光明媚 备 2018.03.12日 

