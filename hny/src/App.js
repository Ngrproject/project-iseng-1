import Particles from "react-particles";
import {loadFireworksPreset} from "tsparticles-preset-fireworks"
import { Typewriter } from "react-simple-typewriter";
import { useState } from "react";
import Countdown from "react-countdown";
function App() {
  const [newYearMessage, setNewYearMessage] = useState(["NGR", 'PROJECT', 'MENUNGGU', 'TAHUN BARU', '2024'])
  const particleinitialization = async (engine) => {
    await loadFireworksPreset(engine)
  }

  function timeleft() {
    const newYearDate = new Date ("january 1, 2024 00:00:00").getTime()
    const nowDate = new Date ().getTime()
    const remainingTime = newYearDate - nowDate
    return remainingTime
  }
  return (
    <>
<Particles
init={particleinitialization}
options={{preset: "fireworks"}}
/>
<div className="flex flex-col justify-center items-center min-h-screen gap-4">
  <span className="text-white text-4xl font-bold px-4 z-50">
   <Typewriter words={newYearMessage}
   loop={false}
   cursorStyle={"_"}
   cursor
   />
  </span>
<div className="z-50 text-white font-bold text-2xl">
<Countdown date={Date.now() + timeleft()} onComplete={()=> setNewYearMessage(
  ["Selamat", "Tahun Baru", "2025"])}
/>

</div>
</div>
</>
  );
}

export default App;
