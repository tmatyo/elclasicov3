import { BannerProps } from "@/types/app";
import RealMadridLogo from "./RealMadridLogo";
import BarcelonaLogo from "./BarcelonaLogo";

export default function Banner({ awayTeam, homeTeam, isPlanned }: BannerProps) {
	const getLogo = (team: string) => (team.includes("Barcelona") ? <BarcelonaLogo /> : <RealMadridLogo />);

	return (
		<div className="grid grid-cols-[repeat(auto-fit,minmax(100px,1fr))] w-full mx-auto text-center my-8">
			{isPlanned ? (
				<>
					<div>
						{getLogo(homeTeam)}
						<h2 className="mt-8 font-bold md:mt-0 sm:hidden">{homeTeam}</h2>
					</div>
					<div className="pt-37.5 md:pt-25 sm:pt-6.25 sm:hidden">
						<h2>VS</h2>
					</div>
					<div>
						{getLogo(awayTeam)}
						<h2 className="mt-8 font-bold md:mt-0 sm:hidden">{awayTeam}</h2>
					</div>
				</>
			) : (
				<p>Nie je naplánované žiadne El clasico :(</p>
			)}
		</div>
	);
}
