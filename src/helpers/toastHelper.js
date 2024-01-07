import { toast } from "react-toastify";

const displayToast = (message, type = "success") => {
  const options = {
    position: "bottom-right",
    autoClose: 2000
  };

  if (type === "success") {
    toast.success(message, options);
  } else if (type === "error") {
    toast.error(message, options);
  }
};

export default displayToast;