// Generated by gencpp from file bumperbot_examples/AddTwointsResponse.msg
// DO NOT EDIT!


#ifndef BUMPERBOT_EXAMPLES_MESSAGE_ADDTWOINTSRESPONSE_H
#define BUMPERBOT_EXAMPLES_MESSAGE_ADDTWOINTSRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace bumperbot_examples
{
template <class ContainerAllocator>
struct AddTwointsResponse_
{
  typedef AddTwointsResponse_<ContainerAllocator> Type;

  AddTwointsResponse_()
    : sum(0)  {
    }
  AddTwointsResponse_(const ContainerAllocator& _alloc)
    : sum(0)  {
  (void)_alloc;
    }



   typedef int64_t _sum_type;
  _sum_type sum;





  typedef boost::shared_ptr< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> const> ConstPtr;

}; // struct AddTwointsResponse_

typedef ::bumperbot_examples::AddTwointsResponse_<std::allocator<void> > AddTwointsResponse;

typedef boost::shared_ptr< ::bumperbot_examples::AddTwointsResponse > AddTwointsResponsePtr;
typedef boost::shared_ptr< ::bumperbot_examples::AddTwointsResponse const> AddTwointsResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator1> & lhs, const ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator2> & rhs)
{
  return lhs.sum == rhs.sum;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator1> & lhs, const ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace bumperbot_examples

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b88405221c77b1878a3cbbfff53428d7";
  }

  static const char* value(const ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb88405221c77b187ULL;
  static const uint64_t static_value2 = 0x8a3cbbfff53428d7ULL;
};

template<class ContainerAllocator>
struct DataType< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bumperbot_examples/AddTwointsResponse";
  }

  static const char* value(const ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
"#Response\n"
"int64 sum\n"
;
  }

  static const char* value(const ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.sum);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct AddTwointsResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::bumperbot_examples::AddTwointsResponse_<ContainerAllocator>& v)
  {
    s << indent << "sum: ";
    Printer<int64_t>::stream(s, indent + "  ", v.sum);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BUMPERBOT_EXAMPLES_MESSAGE_ADDTWOINTSRESPONSE_H
