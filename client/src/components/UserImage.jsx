import { Box } from "@mui/material";

const UserImage = ({ image, size = "60px" }) => {
  return (
    <Box width={size} height={size}>
      <img
        style={{ objectFit: "cover", borderRadius: "50%" }}
        width={size}
        height={size}
        alt="user"
        src={
          // `${process.env.REACT_APP_BACKEND_URL}assets/${image}`
          `http://192.168.49.2:31231/assets/${image}`
          // new URL(`assets/${image}`, process.env.REACT_APP_BACKEND_URL)
      }
      />
    </Box>
  );
};

export default UserImage;
