export interface BannerProps {
	awayTeam: string;
	homeTeam: string;
	isPlanned: boolean;
}

export interface StatProps {
	data: FetchResultStats[];
}

export interface FixtureProps {
	data: FetchResultFixtures[];
}

export interface CountdownProps {
	time: string;
	passMatchTimeToParent: (matchTime: date) => void;
}

export interface ScheduleProps {
	data: FetchResultSchedule[];
}

export interface UseFetchResult<T> {
	data: T | null;
	error: Error | null;
}

export interface FetchResultSchedule {
	id: number;
	away_team: string;
	home_team: string;
	time: string;
	created_at: string;
	time_parsed: string;
}

export interface FetchResultStats {
	id: number;
	matches: number;
	barca: number;
	draw: number;
	real: number;
	barca_goals: number;
	real_goals: number;
	avg_attendance: number;
	created_at: string;
}

export interface FetchResultFixtures {
	id: number;
	date: string;
	home_team: string;
	away_team: string;
	score: string;
	winner: string;
	event: string;
	attendance: string;
	link: string;
	created_at: string;
}

export interface FetchResultData {
	schedule: FetchResultSchedule[] | null;
	stats: FetchResultStats[] | null;
	fixtures: FetchResultFixtures[] | null;
}
